import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F  # Add this import
import gymnasium as gym
import matplotlib.pyplot as plt

class PolicyNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(PolicyNetwork, self).__init__()

        self.linear1 = nn.Linear(input_size, 16)
        self.activation1 = nn.ReLU()
        self.linear2 = nn.Linear(16, 16)
        self.activation2 = nn.ReLU()
        self.linear3 = nn.Linear(16, 16)
        self.activation3 = nn.ReLU()
        self.output_layer = nn.Linear(16, output_size)

        nn.init.xavier_uniform_(self.linear1.weight)
        nn.init.xavier_uniform_(self.linear2.weight)
        nn.init.xavier_uniform_(self.linear3.weight)
        nn.init.xavier_uniform_(self.output_layer.weight)

    def forward(self, inputs):
        x = self.activation1(self.linear1(inputs))
        x = self.activation2(self.linear2(x))
        x = self.activation3(self.linear3(x))
        x = self.output_layer(x)
        return x

class PolicyGradient:
    def __init__(self, input_size, output_size, lr):
        self.model = PolicyNetwork(input_size, output_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)

    def predict(self, state):
        state = torch.FloatTensor(state)
        logits = self.model(state)
        return F.softmax(logits, dim=-1)  # Softmax to get action probabilities

    def update(self, returns, log_probs):
        loss = 0
        for log_prob, G in zip(log_probs, returns):
            loss += -log_prob * G

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

def choose_action(state, policy_network):
    action_probs = policy_network.predict(state)
    action_dist = torch.distributions.Categorical(action_probs)
    action = action_dist.sample()
    return action.item(), action_dist.log_prob(action)

def compute_returns(rewards, gamma):
    returns = []
    G = 0
    for reward in reversed(rewards):
        G = reward + gamma * G
        returns.insert(0, G)
    return returns

def train_policy_gradient(env, policy_network, episodes, gamma, render_interval, average_window):
    rewards_per_episode = []
    average_rewards = []

    plt.figure(figsize=(12, 6))
    reward_line, = plt.plot([], [], label='Reward per Episode')
    average_line, = plt.plot([], [], label='Moving Average Reward')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Episode Reward and Moving Average Reward over Time')
    plt.legend()

    for episode in range(episodes):
        if episode % render_interval == 0 and episode != 0:
            env = gym.make("ALE/Frogger-ram-v5", render_mode="human")
        else:
            env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array")

        state, _ = env.reset()
        done = False
        total_reward = 0
        rewards = []
        log_probs = []

        while not done:
            action, log_prob = choose_action(state, policy_network)
            next_state, reward, done, _, info = env.step(action)

            rewards.append(reward)
            log_probs.append(log_prob)

            state = next_state
            total_reward += reward

            if done:
                break

        rewards_per_episode.append(total_reward)
        returns = compute_returns(rewards, gamma)
        returns = torch.FloatTensor(returns)
        policy_network.update(returns, log_probs)

        if len(rewards_per_episode) >= average_window:
            moving_average = np.mean(rewards_per_episode[-average_window:])
        else:
            moving_average = np.mean(rewards_per_episode)
        average_rewards.append(moving_average)

        reward_line.set_data(range(episode + 1), rewards_per_episode)
        average_line.set_data(range(episode + 1), average_rewards)
        plt.xlim(0, episode + 1)
        plt.ylim(0, max(max(rewards_per_episode), max(average_rewards)) + 10)
        plt.pause(0.01)

        print(f"Episode: {episode}, Total Reward: {total_reward}, Moving Average Reward (last {average_window} episodes): {moving_average:.2f}")

        if episode % 100 == 0:
            plt.savefig("src/policy_gradient_frogger_rewards.png")

    env.close()

# HYPERPARAMETERS
alpha = 0.001  # Learning rate for the optimizer
gamma = 0.90  # Discount factor
episodes = 10000  # Number of episodes
render_interval = 500  # Episode interval for rendering
average_window = 100  # Moving average window size

env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array", difficulty=0)
input_size = env.observation_space.shape[0]
output_size = env.action_space.n
lr = alpha

policy_network = PolicyGradient(input_size, output_size, lr)
train_policy_gradient(env, policy_network, episodes, gamma, render_interval, average_window)

# Save the trained model
torch.save(policy_network.model.state_dict(), "policy_gradient_frogger_model.pth")