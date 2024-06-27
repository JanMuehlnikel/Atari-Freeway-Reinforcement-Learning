
def calculate_reward(initial_reward:int, distance:int, distance_before:int, total_reward, loss_of_live:bool, lives:int, lives_before):
    # add distance to reward going forward 
    if distance > distance_before:
        reward = distance
    else:
        reward = total_reward

    # add reward for moving forward
    initial_reward *= 2
    reward += initial_reward

    # reduce reward when colliding
    if lives < lives_before:
        print(f"loss_of_live with {distance} steps forward")
        if reward <= 2:
            reward = 0
        else:
            reward -= 2

    return reward
