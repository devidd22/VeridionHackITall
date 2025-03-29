import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers 
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from word_choice import *
words = [(item["text"], item["cost"]) for item in data.values()]

# Convert the words and costs into TensorFlow-compatible tensors
word_to_index = {word[0]: idx for idx, word in enumerate(words)}
index_to_word = {idx: word[0] for idx, word in enumerate(words)}
costs = [word[1] for word in words]

# Convert words to indices and costs to tensor
X = [word_to_index[word[0]] for word in words]
y = [cost for cost in costs]

# Create a simple model to predict the next word that beats the given word
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(words), output_dim=64, input_length=1),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Training the model (in reality, you would need more data)
X_train = tf.convert_to_tensor(X, dtype=tf.int32)
y_train = tf.convert_to_tensor(y, dtype=tf.float32)

model.fit(X_train, y_train, epochs=100)

def find_next_word_beating_api(api_word, cost):
    # Find the cost of the API word
    api_cost = cost
    for word_id, word_data in data.items():
        if word_data['text'].lower() == api_word.lower():
            api_cost = word_data['cost']
            break
    
    # Iterate through the words to find the one with higher cost
    for word_id, word_data in data.items():
        if word_data['cost'] > api_cost:
            return word_data['text']
    
    # If no word beats the API word, return a message
    return "No word beats the API word"


# Example usage
api_word = "Fasole"
cost = 7
next_word = find_next_word_beating_api(api_word, cost)
print(f"The next word that beats '{api_word}' is '{next_word}'")