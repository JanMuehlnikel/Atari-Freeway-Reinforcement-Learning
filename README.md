# Implementing RF to play the Atari Freeway game

This project has been implemented with the gymnasium Framework: https://gymnasium.farama.org/environments/atari/freeway/

**The final selected model was v_20.2**

# Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/JanMuehlnikel/Atari-Freeway-Reinforcement-Learning
    cd your-repo
    ```

2. **Create and Activate a New Conda Environment**:
    ```bash
    conda create --name FreewayEnv python=3.10.14
    conda activate FreewayEnv
    ```

3. **Install `pip` in the New Conda Environment**:
    ```bash
    conda install pip
    ```

4. **Install Packages from `requirements.txt`**:
    ```bash
    pip install -r requirements.txt
    ```

# Results

This project implements a reinforcement learning agent using a Deep Q-Network (DQN). Despite our efforts, the agent was only able to learn the baseline method, which involved simply moving up.

## Baseline Method
- The baseline method for the agent was to only move up.

## Implementation Details
- **Algorithm**: Deep Q-Network (DQN)
- **Baseline Method**: Move up
- **Reward Structure**: The reward might have been too high for moving actions and too low for crashing, affecting the learning process.
- **Network Complexity**: The neural network used might have been too simple to accurately approximate the Q-values, limiting the agent's ability to learn more complex behaviors.
- **Training Environment**: Training was conducted on a CPU with a limited training period, which may have constrained the agent's learning capability.

## Possible Improvements
Several factors might have contributed to the agent's limited learning:
1. **Adjusting Rewards**: Modifying the reward structure to balance rewards for moving and penalties for crashing.
2. **Network Architecture**: Using a more complex neural network to better approximate Q-values.
3. **Training Resources**: Utilizing a GPU for training and extending the training period to improve learning efficiency.

These adjustments could potentially enhance the agent's ability to learn beyond the baseline method.

## Successful Try
<img src="succesful_try.gif" alt="Successful Try" width="600" height="400">
<br>
## Bad Try
<img src="bad_try.gif" alt="Bad Try" width="600" height="400">
<br>
## DQN Learning Curve

![Rewards](freeway/dqn/figures/v_20.2/rewards_figure.png)


