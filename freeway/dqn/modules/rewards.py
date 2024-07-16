import json

# Rewards
reward_settings = {
    "crash": -5,
    "finishing": 10,
    "up": 1,
    "down": -1,
    "nothing": -0.25,
    "standard_add": 0,
    "clipping_min_reward": -1,
    "clipping_max_reward": 1
    }

def save_rewards(MODEL_VERSION, path=f"reward_settings/"):
    with open(path + f"{MODEL_VERSION}_reward_settings.json", "w") as json_file:
        json.dump(reward_settings, json_file, indent=4)

def action_based_reward(total_reward, crashed, action, y_pos, prev_y_pos, game_reward):
    gained_reward = 0


    # apply rewards
    # negative reward for death
    if crashed == 1:
        gained_reward += reward_settings["crash"]

    # reward chicken reaching end
    if game_reward == 1:
        gained_reward += reward_settings["finishing"]

    # more penalty / reward for moving backwards / up when further down the road
    if action == 0:
        gained_reward += reward_settings["nothing"]
    if action == 1:
        gained_reward += reward_settings["up"]
    if action == 2:
        gained_reward += reward_settings["down"]

    """
    if action == 1:
        if y_pos > 5:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 10:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 15:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 20:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 25:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 30:
            gained_reward += reward_settings["standard_add"]
        
        if y_pos > 35:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 40:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 45:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 50:
            gained_reward += reward_settings["standard_add"]

        if y_pos > 55:
            gained_reward += reward_settings["standard_add"]

    if action == 2:
        if y_pos > 5:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 10:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 15:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 20:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 25:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 30:
            gained_reward -= reward_settings["standard_add"]
        
        if y_pos > 35:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 40:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 45:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 50:
            gained_reward -= reward_settings["standard_add"]

        if y_pos > 55:
            gained_reward -= reward_settings["standard_add"]
    """


    # Apply reward clipping

    #clipped_gained_reward = max(min(gained_reward, reward_settings["clipping_max_reward"]), reward_settings["clipping_min_reward"])

    total_reward += gained_reward

    return total_reward, gained_reward