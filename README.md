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

## 🗄️ Dataset Details

### 🧪 Dataset Type: Synthetic
This project uses a **Synthetic Financial Impulse Dataset** because real-world behavioral datasets containing high-resolution transaction metadata and labeled "impulse" vs "planned" tags are generally private or unavailable for public research.

### ⚙️ Generation Logic
The data was generated using a custom script ([generate_data.py](file:///d:/SEM8/BA/Hack/data/generate_data.py)) with the following parameters:
- **Volume**: 20,000 transaction records.
- **User Base**: 500 unique user profiles.
- **Distribution**: Base spending for each user is randomized between \$2,000 and \$10,000. Individual transaction amounts follow a normal distribution centered around the user's daily average.
- **Behavioural Rules**: 
  - **Discretionary Spending**: Categories like *Fashion*, *Electronics*, and *Entertainment* are tagged as high-impulse triggers.
  - **Temporal Factors**: Late-night transactions (10 PM – 2 AM) and end-of-month activity are weighted higher for impulse risk.
  - **Spike Detection**: Any purchase exceeding 15% of the user's average spend is flagged as a potential impulse spike.

### 📋 Feature Description

| Feature | Description |
| :--- | :--- |
| `user_id` | Unique identifier for the user. |
| `transaction_time` | Timestamp of the transaction. |
| `amount` | Transaction value in USD. |
| `merchant_category` | Category of spend (e.g., Grocery, Fashion, Bills). |
| `night_transaction` | Binary flag (1 if between 10 PM and 2 AM). |
| `discretionary_category`| Binary flag (1 if category is non-essential). |
| `spending_spike` | Binary flag (1 if amount > 15% of user avg). |
| `short_time_gap` | Binary flag (1 if transaction occurs shortly after another). |
| `end_month_flag` | Binary flag (1 if transaction is after the 25th). |
| `impulse_label` | **Target Variable**: 1 if impulse score ≥ 3, otherwise 0. |

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
3. **Navigate & Explore**: 
   - Use the **sidebar** to find different User IDs (IDs 4, 7, and 11 are great for high-risk examples!).
   - Use the **Tabs** at the top to switch between analytics, the simulator, and the predictor.

## 🧠 Machine Learning Details
- **RandomForestClassifier**: Trained on transaction-level features to identify impulse hits.
- **K-Means Clustering**: Segments users into profiles like "Stable Budget Spender" or "High-Risk Impulse Spender".
- **Dynamic Advice Engine**: Threshold-based recommendations that adapt to both user data and simulated behaviors.

## 🔍 Data & ML Methodology

- **Data Generation**: Uses a sophisticated synthetic data engine (`generate_data.py`) creating realistic user profiles based on mean-spend distributions.
- **Random Forest Classifier**: Handles the complex interaction between transaction variables to predict "Impulse" labels.
- **K-Means Clustering**: Groups users into behavioral personas (e.g., "Stable Budget Spender").
- **PCA**: Reduces high-dimensional user features into a 2D space for intuitive visual benchmarking.

---

## 📊 Model Performance

The predictive engine is built on a robust Random Forest architecture with the following validated metrics:

- **ROC-AUC**: 0.90
- **Accuracy**: 83%
- **High-Risk Recall**: 75%
- **F1 Score (High Risk)**: 0.64

The model demonstrates strong discrimination ability while maintaining a balanced detection rate for impulsive users.

## 📈 Key Behavioural Insights

Analysis of the model's feature importance and user clusters revealed several critical patterns:
- **Discretionary Spending Ratio**: This is the strongest predictor of impulse behaviour across all user segments.
- **Late-Night Volatility**: Transactions occurring between 10 PM and 2 AM show a significantly higher impulse probability score.
- **Relative Spending Spikes**: Purchases that exceed a user's personal average by more than 15% are a leading indicator of impulsive hits.
- **Transaction Frequency**: Users with frequent short time-gaps between purchases exhibit higher behavioral volatility and overall risk.

## 🧠 Model Selection Rationale

During development, multiple sampling techniques were evaluated:
- **SMOTE (Synthetic Minority Over-sampling Technique)**: Experimented with to improve minority class (High Risk) detection.
- **Baseline Balanced-Weight Model**: Although SMOTE was tested, the original model provided **better overall discriminatory performance (ROC-AUC 0.90)** and higher stability while maintaining strong recall (75%). 

As a result, the **baseline balanced-weight Random Forest model** was selected for production deployment in this dashboard to ensure reliable and consistent user profiling.

---

## 🤝 Hackathon Context
This project was built to demonstrate how AI can be a "Financial Co-pilot" rather than just a tracking tool. By focusing on **predictive simulation**, we move from backward-looking reports to forward-looking financial health management.
