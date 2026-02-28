# 💳 Financial Impulse Behaviour Dashboard

> **🏆 Hackathon Submission:** This project was developed to provide actionable insights into financial health by identifying and predicting impulsive spending patterns using Machine Learning.

An interactive, premium Streamlit dashboard designed to help users understand their "Financial Impulse" profile. It combines descriptive analytics with predictive modeling to provide a 360-degree view of spending behavior.

---

## 🎯 Project Objective

The goal of this project is to bridge the gap between raw transaction data and behavioral psychology. By analyzing spending spikes, night-time activity, and frequency of discretionary purchases, the dashboard helps users:
1. **Identify** high-risk spending patterns.
2. **Understand** the behavioral drivers behind their impulses.
3. **Simulate** how changing specific habits can improve their financial health score.

---

## ✨ Premium Features

### 1. 📊 User Analytics Hub (Tab 1)
- **Risk Score Metrics**: Direct visibility into a user's risk level (Low, Medium, High).
- **Personalized PCA Benchmarking**: A visualization showing where the user sits within broader behavioral clusters (marked with a 🔴 star).
- **Feature Importance**: Uses the Random Forest model to show which factors (e.g., spending spikes, night transactions) most affect the user's score.

### 2. 🧠 "What-If" Behavioral Simulator (Tab 2)
- **Interactive Habit Adjustment**: Use the sidebar sliders to simulate changes in your behavior (e.g., reducing late-night shopping).
- **Real-Time Guidance**: Watch the "Simulated Risk Score" and "Simulated Recommendation" update instantly as you move the sliders.

### 3. 💸 Live Transaction Predictor (Tab 3)
- **Pre-purchase Validation**: Enter a potential transaction's amount, category, and time.
- **Impulse Probability**: Get a % probability and clear "Impulse" vs "Planned" classification before you hit "Buy".

---

## 📂 Project Structure

```text
├── app.py                # Main Streamlit dashboard application
├── data/
│   └── generate_data.py  # Script for synthetic data generation (20,000+ transactions)
├── models/               # Model artifacts & Scalers
│   ├── impulse_model.joblib  # Trained Random Forest Classifier
│   ├── scaler.joblib         # StandardScaler for feature normalization
│   └── user_features.joblib  # Pre-processed user-level behavioral metrics
├── notebooks/            # Research & Model Training
│   └── Financial_Impulse_Behaviour_Detection.ipynb
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 📖 How to Interpret the Dashboard

### 🔴 High-Risk vs 🟢 Low-Risk Users
- **Low Risk**: Usually characterized by consistent budgeting, fewer spending spikes, and most transactions occurring during daylight hours.
- **High Risk**: Identified by frequent discretionary spending (Fashion/Electronics), late-night transactions, and short time gaps between purchases.
- **Try it out**: Select **User ID 7** or **User ID 11** in the sidebar to see examples of users needing intervention!

### Using the "What-If" Sliders
The sliders allow you to see the *power of change*. 
- **Example**: If you have a high "Night Trans. Ratio", move the slider down to simulate shifting your shopping to the daytime. You will see your simulated risk score drop and your recommendation become more positive.

### Understanding the Predictor
The predictor uses a rule-based logic derived from the model's training:
- **Impulse Hit**: Transactions that occur at night, are discretionary, and represent a significant spike relative to your average spend.
- **Planned Hit**: Transactions made during typical hours and for essential categories like Bills or Groceries.

---

## 🛠️ Installation & Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

## 🔍 Data & ML Methodology

- **Data Generation**: Uses a sophisticated synthetic data engine (`generate_data.py`) creating realistic user profiles based on mean-spend distributions.
- **Random Forest Classifier**: Handles the complex interaction between transaction variables to predict "Impulse" labels.
- **K-Means Clustering**: Groups users into behavioral personas (e.g., "Stable Budget Spender").
- **PCA**: Reduces high-dimensional user features into a 2D space for intuitive visual benchmarking.

---

## 🤝 Hackathon Context
This project was built to demonstrate how AI can be a "Financial Co-pilot" rather than just a tracking tool. By focusing on **predictive simulation**, we move from backward-looking reports to forward-looking financial health management.
