Absolutely! Here’s a **full, professional, and highly detailed README** for your Shopper Purchase Prediction KNN project. I’ve structured it to be GitHub-ready, easy to read, and informative for both technical and non-technical users.

---

# 🛒 Shopper Purchase Prediction App (KNN)

## Table of Contents

1. [Overview](#overview)
2. [Project Goal](#project-goal)
3. [Features](#features)
4. [Input Fields](#input-fields)
5. [Output Explanation](#output-explanation)
6. [Model Details & Algorithm](#model-details--algorithm)
7. [Model Performance](#model-performance)
8. [Limitations & Future Improvements](#limitations--future-improvements)
9. [How to Run the App](#how-to-run-the-app)
10. [Dependencies](#dependencies)
11. [About the Author](#about-the-author)

---

## Overview

This web application predicts whether a shopper is **likely to make a purchase** on an e-commerce website using behavioral data. The app is built with **Streamlit** for an interactive web interface and leverages a **K-Nearest Neighbors (KNN)** model trained on historical shopper behavior.

It comes with a **futuristic neon UI**, interactive input fields, random sample generator, and animated prediction cards for a visually appealing experience.

---

## Project Goal

The goal of this project is to **analyze shopper behavior** and provide predictions that help e-commerce platforms:

* Identify potential buyers.
* Optimize marketing campaigns.
* Improve user experience by understanding visitor behavior patterns.

---

## Features

* Predict whether a shopper will purchase (`LIKELY` or `NOT likely`).
* Confidence score for the prediction.
* Random sample generation for quick testing.
* Interactive 3D floating input fields.
* Neon futuristic animated UI with background effects.
* Detailed explanations of each input and output field.

---

## Input Fields

| Input                    | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| Administrative           | Number of admin pages visited (integer).                              |
| Administrative Duration  | Time spent on admin pages (seconds).                                  |
| Informational            | Number of informational pages visited (integer).                      |
| Informational Duration   | Time spent on informational pages (seconds).                          |
| Product Related          | Number of product-related pages visited (integer).                    |
| Product Related Duration | Time spent on product-related pages (seconds).                        |
| Bounce Rates             | Fraction of visits where shoppers leave immediately (0–1).            |
| Exit Rates               | Fraction of visits where shoppers exit a page (0–1).                  |
| Page Values              | Estimated page value in dollars.                                      |
| Special Day              | Closeness to a special day/event (0 = not special, 1 = very special). |
| Weekend                  | 0 = weekday, 1 = weekend.                                             |
| Browser                  | Browser code (1–13).                                                  |
| Region                   | Shopper’s region code (1–9).                                          |
| Traffic Type             | Traffic source code (1–20).                                           |
| Operating Systems        | Shopper’s OS code (1–8).                                              |
| Month                    | Month of visit (`Jan` to `Dec`).                                      |
| Visitor Type             | Returning\_Visitor / New\_Visitor / Other.                            |

> The app also supports a **Random Sample Generator** to automatically fill inputs for quick testing.

---

## Output Explanation

* **LIKELY to make a purchase:** Shopper is predicted to buy something.
* **NOT likely to make a purchase:** Shopper is predicted not to buy anything.
* **Confidence:** Probability score (0 to 1) indicating certainty of prediction.

**Visualization:**

* ✅ `LIKELY` predictions appear in a green animated bomb card.
* ❌ `NOT likely` predictions appear in a red animated bomb card.

---

## Model Details & Algorithm

**Algorithm Used:** **K-Nearest Neighbors (KNN)**

* KNN is a **supervised learning algorithm**.
* It calculates **distance metrics** (like Euclidean distance) between the input sample and training data.
* It finds the **k nearest neighbors** and predicts the class based on **majority voting**.

**Why KNN:**

* Simple and easy to understand.
* Effective for small-to-medium sized tabular datasets.
* No training phase (lazy learning) makes it flexible for new data.

**Data Used for Training:**

* Number of pages visited by category.
* Time spent on each page type.
* Bounce rates and exit rates.
* Special day indicator.
* Traffic type, browser, OS, month, region, visitor type.

---

## Model Performance

**Accuracy:** `0.8694` (\~87%)

**Confusion Matrix:**

| Actual \ Predicted | False | True |
| ------------------ | ----- | ---- |
| **False**          | 1998  | 86   |
| **True**           | 236   | 146  |

**Classification Report:**

| Class | Precision | Recall | F1-score | Support |
| ----- | --------- | ------ | -------- | ------- |
| False | 0.89      | 0.96   | 0.93     | 2084    |
| True  | 0.63      | 0.38   | 0.48     | 382     |

**Averages:**

* Macro Average: Precision 0.76, Recall 0.67, F1-score 0.70
* Weighted Average: Precision 0.85, Recall 0.87, F1-score 0.86

> **Interpretation:** The model is excellent at predicting **non-purchasers** but has lower accuracy in predicting **purchasers**. To improve, consider class balancing, feature scaling, or using ensemble methods.

---

## Limitations & Future Improvements

* KNN may not scale well with very large datasets.
* Model struggles with **imbalanced classes** (more non-purchasers than purchasers).
* No feature scaling applied; this can affect distance calculations.
* Future improvements:

  * Apply **StandardScaler or MinMaxScaler** for features.
  * Tune K-value and distance metric.
  * Try **Random Forest, XGBoost, or Logistic Regression** for higher accuracy.
  * Include more behavioral or demographic features for richer prediction.

---

## How to Run the App

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the URL displayed in your browser (usually `http://localhost:8501`)

**Optional:** Use the “🎲 Generate Random Sample” button to test predictions quickly.

---

## Dependencies

* `streamlit` – for web app interface.
* `pandas` – for data manipulation.
* `numpy` – for numeric operations.
* `scikit-learn` – for KNN and model evaluation.
* `joblib` – for saving/loading the trained model.

**Example `requirements.txt`:**

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## About the Author

Made with ❤️ by **Siddhant Patel**

* GitHub: [https://github.com/siddhantpatel](https://github.com/siddhantpatel)
* Passionate about **Data Science, Machine Learning, and AI**.


---



