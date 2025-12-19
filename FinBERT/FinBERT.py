from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert')
model = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert')

# Text input for sentiment analysis
text = "The company's stock price has been soaring due to strong earnings growth."

# Tokenize the input text
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# The output logits (before softmax)
logits = outputs.logits

# Apply softmax to get probabilities for each sentiment class
softmax = torch.nn.Softmax(dim=-1)
probabilities = softmax(logits)

# Get sentiment class probabilities
positive_score = probabilities[0][0].item()  # Probability of positive sentiment
neutral_score = probabilities[0][1].item()   # Probability of neutral sentiment
negative_score = probabilities[0][2].item()  # Probability of negative sentiment

# Print the scores
print(f"Positive: {positive_score:.4f}")
print(f"Neutral: {neutral_score:.4f}")
print(f"Negative: {negative_score:.4f}")


# example output will be
Positive: 0.32
Neutral: 0.51
Negative: 0.17

# This means the model thinks the text is 32% likely to be positive, 51% neutral, and 17% negative.

