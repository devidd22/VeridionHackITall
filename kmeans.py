from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from collections import Counter

# Load dataset
df = pd.read_json("data_to_learn.json")

# Apply TF-IDF vectorization
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_tfidf = vectorizer.fit_transform(df["word"])  # Transform input words

# Reduce dimensionality to capture more semantic meaning
svd = TruncatedSVD(n_components=10, random_state=42)
X = svd.fit_transform(X_tfidf)

y = df["counter-word"]  # Target output

# Train a KNN model to predict counter-words
knn_model = KNeighborsClassifier(n_neighbors=7, metric='cosine')  # Increased neighbors and changed distance metric
knn_model.fit(X, y)

# Function to predict multiple counter-words
def predict_counter_word(new_word, num_results=10):
    new_word_vec = vectorizer.transform([new_word])  # Transform new word
    new_word_vec = svd.transform(new_word_vec)  # Apply dimensionality reduction
    distances, indices = knn_model.kneighbors(new_word_vec, n_neighbors=num_results)  # Get nearest neighbors
    
    predictions = y.iloc[indices[0]].values  # Get the predicted words
    return np.random.choice(predictions)  # Randomly select one from closest matches

# Function to predict counter-word with frequency
def predict_counter_word_most_frequent(new_word, num_predictions=5):
    predictions = []
    
    for _ in range(num_predictions):  # Run multiple times to see variation
        predicted_counter_word = predict_counter_word(new_word)  # Get prediction from KNN model
        predictions.append(predicted_counter_word)  # Add to list
    
    # Count the frequency of each predicted word
    prediction_counts = Counter(predictions)
    
    # Return the counter-word with the highest frequency
    most_frequent_counter_word = prediction_counts.most_common(1)[0][0]
    
    return most_frequent_counter_word

print(predict_counter_word_most_frequent(""))
