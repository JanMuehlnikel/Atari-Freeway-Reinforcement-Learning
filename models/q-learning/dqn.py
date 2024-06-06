import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import random
import gymnasium as gym
from collections import namedtuple, deque, defaultdict
import matplotlib.pyplot as plt
import pickle
from IPython.display import clear_output

class FullyConnectedModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(FullyConnectedModel, self).__init__()

        # Define layers with ReLU activation
        self.linear1 = nn.Linear(input_size, 16)
        self.activation1 = nn.ReLU()
        self.linear2 = nn.Linear(16, 16)
        self.activation2 = nn.ReLU()
        self.linear3 = nn.Linear(16, 16)
        self.activation3 = nn.ReLU()

        # Output layer without activation function
        self.output_layer = nn.Linear(16, output_size)

        # Initialization using Xavier uniform (a popular technique for initializing weights in NNs)
        nn.init.xavier_uniform_(self.linear1.weight)
        nn.init.xavier_uniform_(self.linear2.weight)
        nn.init.xavier_uniform_(self.linear3.weight)
        nn.init.xavier_uniform_(self.output_layer.weight)

    def forward(self, inputs):
        # Forward pass through the layers
        x = self.activation1(self.linear1(inputs))
        x = self.activation2(self.linear2(x))
        x = self.activation3(self.linear3(x))
        x = self.output_layer(x)
        return x

class QNetwork:
    def __init__(self, input_size, output_size, lr):
        self.model = FullyConnectedModel(input_size, output_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()

    def predict(self, state):
        state = torch.FloatTensor(state)
        with torch.no_grad():
            return self.model(state).cpu().numpy()

    def update(self, state, target):
        state = torch.FloatTensor(state)
        target = torch.FloatTensor(target)

        self.optimizer.zero_grad()
        output = self.model(state)
        loss = self.criterion(output, target)
        loss.backward()
        self.optimizer.step()

def choose_action(state, q_network, epsilon, action_space):
    if random.random() < epsilon:
        return action_space.sample()  # Explore
    else:
        q_values = q_network.predict(state)
        return np.argmax(q_values)  # Exploit

def train_dqn(env, q_network, episodes, alpha, gamma, epsilon, epsilon_min, epsilon_decay, render_interval, average_window):
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

        while not done:
            action = choose_action(state, q_network, epsilon, env.action_space)
            next_state, reward, done, _, info = env.step(action)

            next_q_values = q_network.predict(next_state)
            max_next_q_value = np.max(next_q_values)
            target_q_value = reward + gamma * max_next_q_value

            q_values = q_network.predict(state)
            q_values[action] = target_q_value
            q_network.update(state, q_values)

            state = next_state
            total_reward += reward

            if done:
                break

        rewards_per_episode.append(total_reward)

        if len(rewards_per_episode) >= average_window:
            moving_average = np.mean(rewards_per_episode[-average_window:])
        else:
            moving_average = np.mean(rewards_per_episode)
        average_rewards.append(moving_average)

        if epsilon > epsilon_min:
            epsilon *= epsilon_decay

        reward_line.set_data(range(episode + 1), rewards_per_episode)
        average_line.set_data(range(episode + 1), average_rewards)
        plt.xlim(0, episode + 1)
        plt.ylim(0, max(max(rewards_per_episode), max(average_rewards)) + 10)
        plt.pause(0.01)

        print(f"Episode: {episode}, Total Reward: {total_reward}, Moving Average Reward (last {average_window} episodes): {moving_average:.2f}, Epsilon: {epsilon:.4f}")

        if episode % 100 == 0:
            plt.savefig("src/dqn_frogger_rewards.png")

    env.close()

# HYPERPARAMETERS
alpha = 0.001  # Learning rate for the optimizer
gamma = 0.99  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_min = 0.01  # Minimum exploration rate
epsilon_decay = 0.995  # Decay rate for exploration
episodes = 10000  # Number of episodes
render_interval = 500  # Episode interval for rendering
average_window = 100  # Moving average window size

env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array", difficulty=0)
input_size = env.observation_space.shape[0]
output_size = env.action_space.n
lr = alpha

q_network = QNetwork(input_size, output_size, lr)
train_dqn(env, q_network, episodes, alpha, gamma, epsilon, epsilon_min, epsilon_decay, render_interval, average_window)

# Save the trained model
torch.save(q_network.model.state_dict(), "dqn_frogger_model.pth")