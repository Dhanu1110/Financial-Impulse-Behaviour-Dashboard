# 💳 Financial Impulse Behaviour Dashboard

An interactive, premium Streamlit dashboard to analyze and predict financial impulse behaviour using machine learning. This project segments users into behavioral personas and provides real-time transaction risk scoring.

## ✨ Premium Features

### 1. 📊 User Analytics Hub
- **Risk Score Metrics**: Direct visibility into a user's risk level and profile.
- **Personalized PCA Benchmarking**: See exactly where you sit within the behavioral clusters (marked with a 🔴 star).
- **Feature Importance**: Understand what factors (e.g., night spending, spikes) are driving your scores.

### 2. 🧠 "What-If" Behavioral Simulator
- **Interactive Sliders**: Adjust your spending ratios (Night Trans., Spikes, Short Gaps).
- **Real-time Prediction**: Watch your simulated risk score and recommendation change instantly as you tweak your behavior.

### 3. 💸 Live Transaction Predictor
- **Pre-purchase Validation**: Enter amount, category, and time of a new transaction.
- **Impulse Probability**: Get a % probability and clear "Impulse" vs "Planned" classification before you buy.

---

## 📂 Project Structure

```text
├── app.py                # Main Streamlit dashboard application
├── data/
│   └── generate_data.py  # Script for synthetic data generation
├── models/               # Pre-trained machine learning assets
│   ├── impulse_model.joblib
│   ├── scaler.joblib
│   └── user_features.joblib
├── notebooks/            # Original logic and experimentation
│   └── Financial_Impulse_Behaviour_Detection.ipynb
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 🛠️ Installation & Usage

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Dashboard**:
   ```bash
   streamlit run app.py
   ```

3. **Navigate & Explore**: 
   - Use the **sidebar** to find different User IDs (IDs 4, 7, and 11 are great for high-risk examples!).
   - Use the **Tabs** at the top to switch between analytics, the simulator, and the predictor.

## 🧠 Machine Learning Details
- **RandomForestClassifier**: Trained on transaction-level features to identify impulse hits.
- **K-Means Clustering**: Segments users into profiles like "Stable Budget Spender" or "High-Risk Impulse Spender".
- **Dynamic Advice Engine**: Threshold-based recommendations that adapt to both user data and simulated behaviors.
