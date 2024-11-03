# Importing TensorFlow
import tensorflow as tf

# Sample dataset: Simple XOR problem
X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [[0], [1], [1], [0]]

# Define a Sequential model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100, verbose=0)

# Make predictions
predictions = model.predict(X_train)
print("Predictions:\n", predictions)