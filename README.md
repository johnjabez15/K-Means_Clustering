# K-Means Clustering – Customer Segmentation

## Overview

This project implements a **K-Means Clustering** model to group customers into distinct segments based on their **age**, **annual income**, and **spending score**.

The model is trained using a custom dataset and deployed through a **Flask** web application, allowing users to input their information and instantly see which customer segment they belong to.

## Project Structure
```
DataScience/
│
├── K_Means_Clustering/
│ ├── dataset/
│ │ └── customer_segmentation_dataset.csv
│ ├── model/
│ │ └── kmeans_model.pkl
│ ├── static/
│ │ └── style.css
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ ├── train_model.py
│ ├── app.py
│ ├── requirements.txt
│ └── README.md
```

## Installation & Setup

1. **Clone the repository**

    ```
    git clone <your-repo-url>
    cd "DataScience/K_Means_Clustering"
    ```

2. **Create a virtual environment (recommended)**

    ```
    python -m venv venv
    source venv/bin/activate   # For Linux/Mac
    venv\Scripts\activate      # For Windows
    ```

3. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

## Dataset

The dataset contains details of customers with the following features:

* **Age** (numeric)
* **Annual Income** (numeric)
* **Spending Score** (numeric)
  
The goal is to group similar customers into **meaningful clusters** such as:
- **High Income, Low Spending**
- **Medium Income, Medium Spending**
- **Low Income, High Spending**
- **Young, High Spending**

## Problem Statement

Understanding customer segmentation is crucial for businesses to personalize marketing strategies. This project uses **unsupervised machine learning** to automatically group customers into segments, helping businesses target the right audience.

## Why K-Means Clustering?

* **Simple yet powerful** unsupervised learning algorithm.
* Groups data based on similarity without requiring labeled data.
* Helps identify natural patterns and segments in datasets.
* Scales well to large datasets.

## How to Run

1. **Train the Model**

    ```
    python train_model.py
    ```

    This will create:

    * `kmeans_model.pkl` – the trained K-Means clustering model.

2. **Run the Flask App**

    ```
    python app.py
    ```

    Visit `http://127.0.0.1:5000/` in your browser.

## Frontend Input Example

Example customer information:

Age: 25
Annual Income: 45000
Spending Score: 77


## Prediction Goal

The application predicts the **customer segment name** (not just cluster number), for example:

Low Income, High Spending


## Tech Stack

* **Python** – Core programming language
* **Pandas & NumPy** – Data manipulation
* **Scikit-learn** – Machine learning model training
* **Flask** – Web framework for deployment
* **HTML/CSS** – Frontend UI design

## Future Scope

* Automate cluster labeling by analyzing cluster centers instead of using hardcoded names.
* Visualize customer segments with interactive plots.
* Integrate with business dashboards for real-time customer analytics.

## Screenshots

**Home Page:**<img width="1920" height="1080" alt="Screenshot (45)" src="https://github.com/user-attachments/assets/eb0fb0d9-49a5-408b-9f87-a6a0bddc3fd9" />


**Result Page:**<img width="1920" height="1080" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/a6a37fd1-30e1-4bcf-9635-eac84455587d" />
