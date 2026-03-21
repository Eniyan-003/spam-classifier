import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load data
data = pd.read_csv("data.csv")

# Features and labels
X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Prediction function
def predict_spam(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]


# Test
if __name__ == "__main__":
    print(predict_spam("Win money now"))