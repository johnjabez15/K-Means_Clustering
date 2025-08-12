# train_model.py
import pandas as pd
from sklearn.cluster import KMeans
import pickle
import os

# Paths
DATA_PATH = os.path.join("dataset", "customer_segmentation_dataset.csv")
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "kmeans_model.pkl")

# Create model directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Drop non-numeric or irrelevant columns
X = df[['Age', 'Annual_Income', 'Spending_Score']]

# Train KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# Save model as pkl file
with open(MODEL_PATH, "wb") as f:
    pickle.dump(kmeans, f)

print(f"✅ Model trained and saved at: {MODEL_PATH}")
