from keras import models, layers, optimizers
import os

def build_dense_dqn(input_shape=(13, 1), ACTIONS_SIZE=3, LEARNING_RATE=0.0001):
    model = models.Sequential()
    
    model.add(layers.Flatten(input_shape=input_shape))
    
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    
    model.add(layers.Dense(ACTIONS_SIZE, activation='linear'))
    
    optimizer = optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
    
    return model

def save_model(model, episode, MODEL_SAVE_INTERVALL, dir="models/"):
    if episode % MODEL_SAVE_INTERVALL == 0:
        os.makedirs(os.path.dirname(dir), exist_ok=True)
        model.save(dir + f"ep_{episode}_model.h5") 

        model.save_weights(dir + f"ep_{episode}.weights.h5")

