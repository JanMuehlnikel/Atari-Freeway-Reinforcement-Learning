def action_based_reward(total_reward, crashed, action, y_pos, max_distance_episode):
    # REWARDS
    crash = -30
    finishing = 50
    half = 25
    quater = 10

    up = 1
    down = -1
    nothing = -0.5

    #apply rewards
    if action == 0:
        total_reward += nothing
    elif action == 1:
        total_reward += up
    elif action == 2:
        total_reward += down

    # rewwad for gaining forward progress
    if y_pos > max_distance_episode:
        total_reward += max_distance_episode

    # negative reward for death
    if crashed == 1:
        total_reward += crash

    # reward chicken reaching quater
    if y_pos == 42:
        total_reward += quater

    # reward chicken reaching half
    if y_pos == 86:
        total_reward += half

    # reward chicken reaching end
    if y_pos >= 175:
        total_reward += finishing

    return total_reward
    


