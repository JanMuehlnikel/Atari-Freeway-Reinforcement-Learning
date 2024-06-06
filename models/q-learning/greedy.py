import gymnasium as gym
import numpy as np
import random
import pickle
from collections import defaultdict
import matplotlib.pyplot as plt

# Initialize environment
env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array", difficulty=0)

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_min = 0.01
epsilon_decay = 0.995
episodes = 10000  # Number of episodes
render_interval = 500 
average_window = 100  # Moving average window size

rewards_per_episode = []
average_rewards = []

# Initialize the plot
plt.figure(figsize=(12, 6))
reward_line, = plt.plot([], [], label='Reward per Episode')
average_line, = plt.plot([], [], label='Moving Average Reward')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Episode Reward and Moving Average Reward over Time')
plt.legend()

# Q-table initialization using defaultdict to handle unseen states
q_table = defaultdict(lambda: np.zeros(env.action_space.n))

# Helper function to choose an action
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[state])  # Exploit

# Helper function to convert state vector to a tuple (to be used as dictionary key)
def state_to_tuple(state):
    return tuple(state)

# Training loop
for episode in range(episodes):
    if episode % render_interval == 0 and episode !=0:
        env = gym.make("ALE/Frogger-ram-v5", render_mode="human")
    else:
        env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array")

    state, _ = env.reset()
    state = state_to_tuple(state)
    done = False
    total_reward = 0
    
    while not done:
        action = choose_action(state)
        next_state, reward, done, _, info = env.step(action)
        next_state = state_to_tuple(next_state)
        
        # Update Q-value
        q_value = q_table[state][action]
        max_next_q_value = np.max(q_table[next_state])
        q_table[state][action] = q_value + alpha * (reward + gamma * max_next_q_value - q_value)
        
        state = next_state
        total_reward += reward
        
        if done:
            break

    # Store reward
    rewards_per_episode.append(total_reward)
    
    # Calculate moving average
    if len(rewards_per_episode) >= average_window:
        moving_average = np.mean(rewards_per_episode[-average_window:])
    else:
        moving_average = np.mean(rewards_per_episode)
    average_rewards.append(moving_average)

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # Update plot
    reward_line.set_data(range(episode + 1), rewards_per_episode)
    average_line.set_data(range(episode + 1), average_rewards)
    plt.xlim(0, episode + 1)
    plt.ylim(0, max(max(rewards_per_episode), max(average_rewards)) + 10)
    plt.pause(0.01)

    if episode % 100 == 0:
        plt.savefig("src/qlearning_greedy.png")

    print(f"Episode: {episode}, Total Reward: {total_reward}, Moving Average Reward (last {average_window} episodes): {moving_average:.2f}, Epsilon: {epsilon:.4f}")

# Close the environment
env.close()

# Save the Q-table
with open("q_table.pkl", "wb") as f:
    pickle.dump(dict(q_table), f)
