import gymnasium
import time

"""
ALE/Frogger-ram-v5: for RAM output with direct information where objects are in the game
ALE/Frogger-v5: For an RGB Image as output 
"""
env = gymnasium.make(
    "ALE/Frogger-ram-v5", 
    render_mode="human",  # (human or rgb_array)
    # mode=2
    difficulty=0
)

print("Action space:", env.action_space)

# Reset the environment
observation = env.reset()
print("Initial observation:", observation)

try:
    step = 0
    while step < 1000:
        # env.render()
        
        # Perform baseline action (Move UP every time)
        if step % 2 == 0:
            action = 0
        else:
            action = 1
        step_result = env.step(action)
        observation, reward, done, loss_of_live, info = step_result

        print(f"Step: {step}, Action: {action}, Reward: {reward}, Loss of Live in this step: {loss_of_live} Lives: {info} Done: {done}")
        
        # Reset the env when the game is over
        if done:
            print("Environment reset")
            observation = env.reset()
            print("New observation after reset:", observation)
            step = 0

        step += 1
finally:
    env.close()
