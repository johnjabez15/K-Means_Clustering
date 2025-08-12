from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained KMeans model
MODEL_PATH = os.path.join("model", "kmeans_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Map cluster numbers to meaningful labels
cluster_labels = {
    0: "High Income, Low Spending",
    1: "Medium Income, Medium Spending",
    2: "Low Income, High Spending",
    3: "Young, High Spending"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        income = float(request.form['income'])
        score = float(request.form['score'])

        # Prepare input for model
        features = np.array([[age, income, score]])
        cluster_number = model.predict(features)[0]
        cluster_name = cluster_labels.get(cluster_number, f"Cluster {cluster_number}")

        return render_template('result.html',
                               age=age,
                               income=income,
                               score=score,
                               cluster_name=cluster_name)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
