from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),  # Flatten the 2D output to 1D for the Dense layer
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.summary()
