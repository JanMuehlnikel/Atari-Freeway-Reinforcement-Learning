import gymnasium as gym
import numpy as np
import random
import pickle
from collections import defaultdict
import matplotlib.pyplot as plt

"""
Atari Frogger from Gymnasium Enviroment:
https://gymnasium.farama.org/environments/atari/frogger/#observations
"""
env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array", difficulty=0)

# HYPERPARAMETERS
alpha = 0.2  # Learning rate (high -> overshoot low -> slow down learning)
gamma = 0.99  # Discount factor (importance of long term reward)
epsilon = 1.0  # Exploration rate ()
epsilon_min = 0.01 # Minimum exploration rate (increase -> more exploreation)
epsilon_decay = 0.995 # Decay Rate (decrease -> more exploreation)
episodes = 10000  # Number of episodes

reward_moving_forward = 3

render_interval = 500 # Episode where game is rendered
average_window = 100  # Moving average window size

rewards_per_episode = []
average_rewards = []

# REWARD PLOT
plt.figure(figsize=(12, 6))
reward_line, = plt.plot([], [], label='Reward per Episode')
average_line, = plt.plot([], [], label='Moving Average Reward')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Episode Reward and Moving Average Reward over Time')
plt.legend()

# Q TABLE
q_table = defaultdict(lambda: np.zeros(env.action_space.n))

# HELPER FUNCTIONS
def choose_action(state):
    """
    Function to choose the action
    """
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[state])  # Exploit

def state_to_tuple(state):
    """
    Function to convert state vector to a tuple
    """
    return tuple(state)

# TRAINING LOOP
for episode in range(episodes):
    # choose between array or human render method
    if episode % render_interval == 0 and episode !=0:
        env = gym.make("ALE/Frogger-ram-v5", render_mode="human")
    else:
        env = gym.make("ALE/Frogger-ram-v5", render_mode="rgb_array")
    
    # reset env
    state, _ = env.reset()
    state = state_to_tuple(state)
    done = False
    total_reward = 0
    
    # round / episode loop (game runs til player looses all his lives)
    while not done:
        # store initial position of frog
        initial_position = env.unwrapped.ale.getRAM()[57]

        # run action
        action = choose_action(state)
        next_state, reward, done, _, info = env.step(action)
        next_state = state_to_tuple(next_state)
        
        # calculate the new position
        new_position = env.unwrapped.ale.getRAM()[57]

        # Additional reward for moving forward
        #if new_position > initial_position:
        #   reward += reward_moving_forward 
        
        # Update Q-value
        q_value = q_table[state][action]
        max_next_q_value = np.max(q_table[next_state])
        q_table[state][action] = q_value + alpha * (reward + gamma * max_next_q_value - q_value)
        
        state = next_state
        total_reward += reward
        
        if done:
            break

    # store reward
    rewards_per_episode.append(total_reward)
    
    # calculate moving average
    if len(rewards_per_episode) >= average_window:
        moving_average = np.mean(rewards_per_episode[-average_window:])
    else:
        moving_average = np.mean(rewards_per_episode)
    average_rewards.append(moving_average)

    # decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # update plot
    reward_line.set_data(range(episode + 1), rewards_per_episode)
    average_line.set_data(range(episode + 1), average_rewards)
    plt.xlim(0, episode + 1)
    plt.ylim(0, max(max(rewards_per_episode), max(average_rewards)) + 10)
    plt.pause(0.01)

    # print out current state
    print(f"Episode: {episode}, Total Reward: {total_reward}, Moving Average Reward (last {average_window} episodes): {moving_average:.2f}, Epsilon: {epsilon:.4f}")

    if episode % 100 == 0:
        plt.savefig("src/qlearning_greedy.png")


env.close()

# save q table
with open("q_table.pkl", "wb") as f:
    pickle.dump(dict(q_table), f)
