def action_based_reward(total_reward, crashed, action, y_pos, prev_y_pos, game_reward):
    gained_reward = 0

    # REWARDS
    crash = -20
    finishing = 20
    up = 1
    down = -0.5
    nothing = -0.25

    standard_add = 0.1

    # apply rewards
    # negative reward for death
    if crashed == 1:
        gained_reward += crash

    # reward chicken reaching end
    if game_reward == 1:
        gained_reward += finishing

    # more penalty / reward for moving backwards / up when further down the road
    if action == 0:
        gained_reward += nothing
    if action == 1:
        gained_reward += up
    if action == 2:
        gained_reward += down

    if action == 1:
        if y_pos > 5:
            gained_reward += standard_add

        if y_pos > 10:
            gained_reward += standard_add

        if y_pos > 15:
            gained_reward += standard_add

        if y_pos > 20:
            gained_reward += standard_add

        if y_pos > 25:
            gained_reward += standard_add

        if y_pos > 30:
            gained_reward += standard_add
        
        if y_pos > 35:
            gained_reward += standard_add

        if y_pos > 40:
            gained_reward += standard_add

        if y_pos > 45:
            gained_reward += standard_add

        if y_pos > 50:
            gained_reward += standard_add

        if y_pos > 55:
            gained_reward += standard_add

    if action == 2:
        if y_pos > 5:
            gained_reward -= standard_add

        if y_pos > 10:
            gained_reward -= standard_add

        if y_pos > 15:
            gained_reward -= standard_add

        if y_pos > 20:
            gained_reward -= standard_add

        if y_pos > 25:
            gained_reward -= standard_add

        if y_pos > 30:
            gained_reward -= standard_add
        
        if y_pos > 35:
            gained_reward -= standard_add

        if y_pos > 40:
            gained_reward -= standard_add

        if y_pos > 45:
            gained_reward -= standard_add

        if y_pos > 50:
            gained_reward -= standard_add

        if y_pos > 55:
            gained_reward -= standard_add



    # Apply reward clipping
    min_reward = -1
    max_reward = 1
    #clipped_reward = max(min(gained_reward, max_reward), min_reward)

    total_reward += gained_reward

    return total_reward, gained_reward