import matplotlib.pyplot as plt

def reward_plot(rewards_per_episode, average_rewards):
    plt.figure(figsize=(12, 6))
    plt.plot(rewards_per_episode, label='Reward per Episode', alpha=0.75)
    plt.plot(average_rewards, label='Moving Average Reward')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Episode Reward and Moving Average Reward over Time')
    plt.legend()
    plt.savefig('figures/rewards_figure.png')

def distance_plot(distance_per_episode):
    plt.figure(figsize=(12, 6))
    plt.plot(distance_per_episode, label='Distance')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('Episode')
    plt.ylabel('Distance')
    plt.title('Distance Travelled Per Episode')
    plt.legend()
    plt.savefig('figures/distances_figure.png')