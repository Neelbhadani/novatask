import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from feature_extraction import extract_features

# Load your training data
with open('data/novatask_training_data.json', 'r') as f:
    dataset = json.load(f)

X = []
y = []
label_map = {"allow": 0, "block": 1, "flag": 2}

for item in dataset:
    feat = extract_features(item)
    X.append(list(feat.values()))
    y.append(label_map.get(item['label'], 0))

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.int32)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=15,
    batch_size=16,
    verbose=1
)

# Save the trained model
model.save('ml/novatask_model.h5')

# Plot and Save Loss Graph
plt.figure(figsize=(8,6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.savefig('ml/loss_plot.png')  # Saves the graph as an image

# Plot and Save Accuracy Graph
plt.figure(figsize=(8,6))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.savefig('ml/accuracy_plot.png')  # Saves the graph as an image

print("✅ Training completed. Model and graphs saved.")
