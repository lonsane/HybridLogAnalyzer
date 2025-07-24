import joblib
from sentence_transformers import SentenceTransformer

model_embedding = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight embedding model
model_classification = joblib.load("models/log_classifier.joblib")


def classify_with_bert(log_message):
    embeddings = model_embedding.encode([log_message])
    probabilities = model_classification.predict_proba(embeddings)[0]
    if max(probabilities) < 0.5:
        return "Unclassified"
    predicted_label = model_classification.predict(embeddings)[0]
    
    return predicted_label


if __name__ == "__main__":
    logs = [
        "Backup completed successfully.",
        "Backup completed successfully.",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "RAID array experienced multiple disk failures and issues",
        "Key system element crashed: element ID Component77"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)