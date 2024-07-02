from keras import models, layers, optimizers

def build_cnn_dqn(input_shape=(210, 160, 1), ACTIONS_SIZE=3, LEARNING_RATE=0.0001):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(512, activation='relu'),
        layers.Dense(ACTIONS_SIZE, activation='linear')
    ])

    optimizer = optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer,
                  loss='mse',  # Mean Squared Error for Q-learning
                  metrics=['accuracy'])

    return model

def build_dense_dqn(input_shape=(12, 1), ACTIONS_SIZE=3, LEARNING_RATE=0.0001):
    model = models.Sequential()
    
    # Flatten the input to (128,) shape to fit into Dense layers
    model.add(layers.Flatten(input_shape=input_shape))
    
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    
    model.add(layers.Dense(ACTIONS_SIZE, activation='linear'))
    
    optimizer = optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
    
    return model