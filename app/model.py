import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = "app/spam_model.pkl"

def train_and_save():
    data = pd.read_csv("data.csv")

    X = data["text"]
    y = data["label"]

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Accuracy
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc * 100:.2f}%")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump((model, vectorizer), f)

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def predict(text):
    model, vectorizer = load_model()
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]


df = pd.read_csv("sms.tsv", sep="\t", names=["label", "text"])
df.to_csv("data.csv", index=False)

if __name__ == "__main__":
    train_and_save()