# 📩 Spam Classifier (AI + FastAPI + UI)

## 🚀 Overview

This project is a full-stack AI application that classifies SMS messages as Spam or Not Spam using Machine Learning.

## 🧠 Features

* Spam detection using Naive Bayes
* FastAPI backend
* Interactive UI
* Model saved using Pickle
* Dockerized application

## 🛠️ Tech Stack

* Python, FastAPI
* Scikit-learn, Pandas
* HTML, CSS, JavaScript
* Docker

## 📊 Model Performance

* Accuracy: ~95% (SMS dataset)

## ⚙️ How It Works

1. User enters message in UI
2. Frontend sends request to FastAPI
3. Model processes text using CountVectorizer
4. Naive Bayes predicts spam/ham
5. Result displayed in UI

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t spam-classifier .
docker run -p 8000:8000 spam-classifier
```

## 📸 Screenshot

(Add screenshot here)

## 🔥 Future Improvements

* Add probability score
* Improve UI
* Deploy to AWS

---

👨‍💻 Developed by Eniyan
