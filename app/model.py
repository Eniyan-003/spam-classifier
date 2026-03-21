import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load data
data = pd.read_csv("data.csv")

X = data["text"]
y = data["label"]

# Vectorize
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

def predict(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]