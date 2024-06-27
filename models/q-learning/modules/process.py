import numpy as np
from collections import deque

def stack_frames(stacked_frames, state, is_new_episode, STATE_SIZE, STACKED_FRAMES_SIZE):
    if is_new_episode:
        # clear stack for new episode
        stacked_frames = deque([np.zeros((STATE_SIZE), dtype=np.int32) for i in range(STACKED_FRAMES_SIZE)], maxlen=4)
        
        # Add the same frame 4 times to the deque since its a new episode
        stacked_frames.append(state)
        stacked_frames.append(state)
        stacked_frames.append(state)
        stacked_frames.append(state)
        
        # Stack the frames with numpy (join all 4 frames)
        stacked_frames_array = np.stack(stacked_frames, axis=2)

    elif not is_new_episode:
        # append new frame and remove oldest frame
        stacked_frames.append(state)

        # Stack the frames with numpy (join all 4 frames)
        stacked_frames_array = np.stack(stacked_frames, axis=2) 

    stack_expanded = stacked_frames_array.reshape((1,) + stacked_frames_array.shape)
    return stack_expanded, stacked_frames

def preprocess_frames(frame):
    
    # resize frame to fit for cnn
    #print("before", frame.shape)
    #frame = np.reshape(frame, (210, 160))
    #print(frame.shape)
    
    # normalize pixel values to [-1, 1]
    frame = frame / 127.5 - 1.0 
    frame = frame.astype(np.float32)

    return frame

    # TODO: flatten