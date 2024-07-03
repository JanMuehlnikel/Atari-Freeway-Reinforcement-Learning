def action_based_reward(total_reward, crashed, action, y_pos, game_reward):
    total_reward_beginning = total_reward
    # REWARDS
    crash = -500
    finishing = 1000
    half = 10
    quater = 5

    up = 20
    down = -20
    nothing = -10

    #apply rewards
    if action == 0:
        total_reward += nothing
        #print(f"nothing: {nothing} ,{y_pos}")
    elif action == 1:
        total_reward += up
        #print(f"up: {up} ,{y_pos}")
    elif action == 2:
        total_reward += down
        #print(f"down: {down} ,{y_pos}")
    """
    # rewwad for gaining forward progress
    if y_pos > max_distance_episode:
        total_reward += max_distance_episode
        print(f"max distance {max_distance_episode}")
    """
    # negative reward for death
    if crashed == 1:
        total_reward += crash
       # print(f"crash {crash} ,{y_pos}")
    """
    # reward chicken reaching quater
    if y_pos == 16 and reached_quater == False:
        total_reward += quater
        print(f"rached quater: {quater} ,{y_pos}")
    """
    # reward chicken for being over quater
    if y_pos >= 16:
        total_reward += quater
        #print(f"rached quater: {quater} ,{y_pos}")
    # reward chicken reaching half
    if y_pos >= 32:
        total_reward += half
        #print(f"rached half: {half} ,{y_pos}")
    # reward chicken reaching end
    if game_reward == 1:
        total_reward += finishing
        #print(f"finsihed: {finishing} ,{y_pos}")

    gained_reward = total_reward - total_reward_beginning

    return total_reward, gained_reward
    


