from model_handler import SentimentModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Add the root directory to sys.path to allow importing from there
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import model_handler

app = FastAPI()

# Add CORS middleware (allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for debugging
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the model
model = SentimentModel(model_path="backend/my_model")


class TextInput(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API"}


@app.post("/predict/")
def predict_sentiment(input: TextInput):
    sentiment = model.predict(input.text)
    return {"sentiment": sentiment}
