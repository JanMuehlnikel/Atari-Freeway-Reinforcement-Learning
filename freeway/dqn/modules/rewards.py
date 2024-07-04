def action_based_reward(total_reward, crashed, action, y_pos, game_reward):
    total_reward_beginning = total_reward
    # REWARDS
    crash = -200
    finishing = 1000
    half = 4
    quater = 2
    threequater = 6

    up = 20
    down = -10
    nothing = -5

    #apply rewards
    if action == 0:
        total_reward += nothing
    elif action == 1:
        total_reward += up
    elif action == 2:
        total_reward += down

    # negative reward for death
    if crashed == 1:
        total_reward += crash

    # reward chicken for being over quater
    if y_pos >= 16:
        total_reward += quater

    # reward chicken reaching half
    if y_pos >= 32:
        total_reward += half

    # reward chicken reaching three quater
    if y_pos >= 48:
        total_reward += threequater

    # positional reward
    if y_pos > 6:
        total_reward += (y_pos -6) / 4

    # reward chicken reaching end
    if game_reward == 1:
        total_reward += finishing

    gained_reward = total_reward - total_reward_beginning

    return total_reward, gained_reward
    


