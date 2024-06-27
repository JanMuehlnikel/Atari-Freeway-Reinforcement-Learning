import random
from collections import deque

class ReplayBuffer:
    def __init__(self, REPLAY_BUFFER_MEMORY, MINI_BATCHES_REPLAY):
        # deque that ther are only max REPLAY_BUFFER_MEMORY items in the list
        # deque = remove oldest item
        self.replay_buffer_memory = REPLAY_BUFFER_MEMORY
        self.mini_batches_replay = MINI_BATCHES_REPLAY
        self.buffer = deque(maxlen=self.replay_buffer_memory)
    
    def add(self, experience):
        # add item to buffer
        self.buffer.append(experience)
    
    def sample(self):
        return random.sample(self.buffer, self.mini_batches_replay) # 16 (MINI_BATCHES_REPLAY) samples to retrain the mdoel