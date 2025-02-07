from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch


class SentimentModel:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        """Load the model and tokenizer from the local directory."""
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, local_files_only=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_path, local_files_only=True)

    def predict(self, text: str) -> str:
        """Predict the sentiment of the given text."""
        inputs = self.tokenizer(text, return_tensors="pt",
                                truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_label = torch.argmax(predictions, dim=1).item()
        labels = {0: "positive", 1: "negative", 2: "neutral"}
        return labels.get(predicted_label, "unknown")
