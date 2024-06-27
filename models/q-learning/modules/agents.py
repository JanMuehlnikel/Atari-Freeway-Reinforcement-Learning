import random
from tqdm import tqdm
import numpy as np

import networks
from replay_buffer import ReplayBuffer

class DQNAgent:
    def __init__(self, REPLAY_BUFFER_MEMORY, MINI_BATCHES_REPLAY, EPSILON, ACTIONS_SIZE, GAMMA, EPSILON_MIN, EPSILON_DECAY_RATE):
        self.MINI_BATCHES_REPLAY = MINI_BATCHES_REPLAY
        self.memory = ReplayBuffer(REPLAY_BUFFER_MEMORY, self.MINI_BATCHES_REPLAY)
        self.EPSILON = EPSILON
        self.ACTIONS_SIZE = ACTIONS_SIZE
        self.GAMMA = GAMMA
        self.EPSILON_MIN = EPSILON_MIN
        self.EPSILON_DECAY_RATE = EPSILON_DECAY_RATE
        self.model = networks.build_dqn()
        self.target_model = networks.build_dqn()
        self.update_target_model()
    
    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())
    
    def remember(self, state, action, reward, next_state, done):
        # flattend_array_state = np.expand_dims(state.reshape(-1), axis=0)
        # flattend_array_next_state = np.expand_dims(next_state.reshape(-1), axis=0)
        self.memory.add((state, action, reward, next_state, done))
    
    def predict_action(self, stacked_array):
        # flatten array for model
        #flattend_array = np.expand_dims(stacked_array.reshape(-1), axis=0)

        if np.random.rand() <= self.EPSILON:
            return random.randrange(self.ACTIONS_SIZE)
        q_values = self.model.predict(stacked_array, verbose=0)

        action = np.argmax(q_values[0])
        #print(q_values)
        #print(q_values[0])
        #print(action)
        return action
    
    def replay(self):
        print("Replay")
        minibatch = self.memory.sample()
        i = 0
        for state, action, reward, next_state, done in tqdm(minibatch):
            i += 1
            
            # Predict Target Q-Values
            target = self.model.predict(state, verbose=0)
            if done:
                # If the episode is done the target Q-value for the taken action is set to the received reward
                target[0][action] = reward
            elif not done:
                # If the episode is not done, the target Q-value for the taken action is updated using the Bellman equation
                t = self.target_model.predict(next_state, verbose=0)[0]
                target[0][action] = reward + self.GAMMA * np.amax(t)
            self.model.fit(state, target, epochs=1, verbose=0)
                
        if self.EPSILON > self.EPSILON_MIN:
            self.EPSILON *= self.EPSILON_DECAY_RATE

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)