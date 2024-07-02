"""
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
"""

def action_based_reward(total_reward, action, distance_travelled, distance_before, current_lives, lives_before):
    # REWARDS
    death = -30
    crossing_road = 50
    reaching_3 = 20

    up = 1
    down = -1
    left = 0
    right = 0
    nothing = -0.5

    #apply rewards
    if action == 0:
        total_reward += nothing
    elif action == 1:
        total_reward += up
    elif action == 2:
        total_reward += right
    elif action == 3:
        total_reward += left
    elif action == 4:
        total_reward += down

    # rewwad for gaining forward progress
    if distance_travelled > distance_before:
        total_reward += distance_travelled

    # negative reward for death
    if current_lives < lives_before:
        total_reward += death

    # reward for get tom pos 3
    if distance_travelled == 3:
        total_reward += reaching_3


    # reward for crossing highway
    if distance_travelled == 6:
        total_reward += crossing_road

    return total_reward
    


