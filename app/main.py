from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(msg: Message):
    result = predict(msg.text)
    return {"prediction": result}

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")