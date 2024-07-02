import numpy as np
from collections import deque

def preprocess_ram(ram_state):
    """
    Reduce the length of the ram array to only the relevant positions.
    RELEVANT RAM SLOTS 
    Reference: (https://github.com/mila-iqia/atari-representation-learning/blob/master/atariari/benchmark/ram_annotations.py)
    """
    ram_state = reduce_state(ram_state)
    relevant_positions = {
        "player_y": 14,
        "score": 103,
        "enemy_car_x": list(range(108, 118))
        }

    # Extract the values for the specified positions into an array
    ram_state = np.array([
        ram_state[relevant_positions["player_y"]],
        ram_state[relevant_positions["score"]],
        *[ram_state[i] for i in relevant_positions["enemy_car_x"]]
    ])
    # normalize
    ram_state = ram_state / 255

    # add batch dimension
    ram_state = np.expand_dims(ram_state, axis=0)

    with open("logs/sample_frame.txt", 'w') as f:
        np.savetxt(f, ram_state.flatten(), fmt='%.6f')

    return ram_state


"""
Reduce Space further
Reference: https://github.com/DionisiusMayr/FreewayGame/blob/main/freeway/freeway.ipynb
"""
def reduce_state(state):
    # Doesn't matter where we were hit
    state[16] = 1 if state[16] != 255 else 0

    # Reduce chicken y-position
    state[14] = state[14] // 3

    for b in range(108, 118):
        # The chicken is in the x-posistion ~49
        if state[b] < 20 or state[b] > 80:
            # We don't need to represent cars far from the chicken
            state[b] = 0
        else:
            # Reduce the cars x-positions sample space
            state[b] = state[b] // 3

    return state