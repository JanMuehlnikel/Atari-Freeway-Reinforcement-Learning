import matplotlib.pyplot as plt
import os

def reward_plot(rewards_per_episode, average_rewards, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(rewards_per_episode, label='Reward per Episode', alpha=0.35)
    plt.plot(average_rewards, label='Moving Average Reward')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Episode Reward and Moving Average Reward over Time')
    plt.legend()
    plt.savefig(f'{dir}rewards_figure.png')

def distance_plot(distance_per_episode, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.plot(distance_per_episode, label='Distance')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Episode')
    plt.ylabel('Distance')
    plt.title('Distance Travelled Per Episode')
    plt.legend()
    plt.savefig(f'{dir}distances_figure.png')

def max_distance_plot(max_distance_per_episode, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.plot(max_distance_per_episode, label='Max Distance')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Episode')
    plt.ylabel('Max Distance In Episode')
    plt.title('Max Distance Travelled Per Episode')
    plt.legend()
    plt.savefig(f'{dir}max_distances_figure.png')