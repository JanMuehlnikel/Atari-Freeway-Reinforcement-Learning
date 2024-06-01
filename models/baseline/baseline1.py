import gymnasium as gym
import time

# Create the Freeway environment with explicit configuration for single-player mode
env = gym.make('ALE/Freeway-v5', render_mode='human', mode=1)

# Reset the environment
observation, info = env.reset()

env.render()

# Main loop
try:
    step = 0
    while step < 1000:  # Run for a fixed number of steps, or change condition as needed
        # Render the environment

        # Move the chicken up every second
        #time.sleep(1)
        
        # Perform the action (move up)
        action = 1  # Action for moving up
        observation, reward, done, truncated, info = env.step(action)
        
        # Log the step, action, reward, and done status
        print(f"Step: {step}, Action: {action}, Reward: {reward}, Done: {done}, Truncated: {truncated}")

        # If the game is over, reset the environment
        if done or truncated:
            observation, info = env.reset()
            print("Environment reset")

        step += 1
finally:
    # Close the environment
    env.close()
