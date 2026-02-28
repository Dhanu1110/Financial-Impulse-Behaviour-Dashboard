import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

st.set_page_config(page_title="Financial Impulse Dashboard", layout="wide")

st.title("💳 Financial Impulse Behaviour Dashboard")

# Load artifacts
model = joblib.load("models/impulse_model.joblib")
scaler = joblib.load("models/scaler.joblib")
user_features = joblib.load("models/user_features.joblib")

# Feature Lists
model_features = [
    'avg_amount', 'amount_std', 'night_ratio', 'weekend_ratio',
    'discretionary_ratio', 'spike_ratio', 'short_gap_ratio',
    'end_month_ratio', 'high_risk'
]

scaler_features = [
    'avg_amount', 'amount_std', 'night_ratio', 'weekend_ratio',
    'discretionary_ratio', 'spike_ratio', 'short_gap_ratio',
    'end_month_ratio'
]

# Sidebar - Selection & Simulator
st.sidebar.header("👤 Dashboard Controls")
user_id = st.sidebar.selectbox("Select User ID", user_features["user_id"])

st.sidebar.markdown("---")
st.sidebar.subheader("📈 What-If Simulator")
st.sidebar.info("Adjust behaviors to see risk impact")

# Simulator Inputs initialized with current user data
user_data = user_features[user_features["user_id"] == user_id].iloc[0]

sim_night = st.sidebar.slider("Night Trans. Ratio", 0.0, 1.0, float(user_data["night_ratio"]))
sim_spike = st.sidebar.slider("Spending Spike Ratio", 0.0, 1.0, float(user_data["spike_ratio"]))
sim_short_gap = st.sidebar.slider("Short Gap Ratio", 0.0, 1.0, float(user_data["short_gap_ratio"]))

# Create Tabs
tab1, tab2, tab3 = st.tabs(["📊 User Analytics", "🧠 Behavior Simulator", "💸 Transaction Tester"])

with tab1:
    st.subheader("📊 User Risk Profile")
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Risk Score", f"{float(user_data['risk_score']):.2f}")
    col2.metric("Risk Level", user_data["risk_level"])
    col3.metric("Behaviour Profile", user_data["behaviour_profile"])
    
    st.info(f"**Current Recommendation:** {user_data['recommendation']}")
    
    col_l, col_r = st.columns(2)
    
    with col_l:
        st.write("### 📈 Feature Importance")
        importances = model.feature_importances_
        fig_imp, ax_imp = plt.subplots(figsize=(10, 6))
        ax_imp.barh(model_features, importances, color='#4A90E2')
        ax_imp.set_title("What drives your impulse score?")
        st.pyplot(fig_imp)
        
    with col_r:
        st.write("### 🔍 Behavioral Clusters (PCA)")
        clustering_features = user_features[scaler_features]
        scaled_data = scaler.transform(clustering_features)
        pca = PCA(n_components=2)
        reduced = pca.fit_transform(scaled_data)
        
        user_idx = user_features[user_features["user_id"] == user_id].index[0]
        
        fig_pca, ax_pca = plt.subplots(figsize=(10, 6))
        scatter = ax_pca.scatter(reduced[:,0], reduced[:,1], c=user_features["cluster"], cmap='viridis', alpha=0.6)
        ax_pca.scatter(reduced[user_idx, 0], reduced[user_idx, 1], c='red', s=200, marker='*', label='You')
        ax_pca.set_title("Where do you fit in?")
        ax_pca.legend()
        st.pyplot(fig_pca)

    st.markdown("---")
    st.write("### 🕵️ Find Other User Personas")
    high_risk_users = user_features[user_features["risk_level"] != "Low"]["user_id"].head(5).tolist()
    st.write(f"Try these High/Medium Risk IDs for different recommendations: **{high_risk_users}**")

with tab2:
    st.subheader("🧠 What-If: Risk Impact Analysis")
    st.write("Predict how your risk score changes based on simulated behavior changes.")
    
    base_risk = float(user_data["risk_score"])
    delta = (sim_night - user_data["night_ratio"]) * 20 + \
            (sim_spike - user_data["spike_ratio"]) * 30 + \
            (sim_short_gap - user_data["short_gap_ratio"]) * 15
            
    simulated_risk = max(0, min(100, base_risk + delta))
    
    c1, c2 = st.columns(2)
    c1.metric("Original Risk", f"{base_risk:.2f}")
    c2.metric("Simulated Risk", f"{simulated_risk:.2f}", delta=f"{simulated_risk - base_risk:.2f}", delta_color="inverse")
    
    st.markdown("### 🔔 Simulated Recommendation")
    if simulated_risk > 75:
        st.error("**URGENT:** High risk of debt. Enable total spending lock for 48 hours for any spike purchase.")
    elif simulated_risk > 50:
        st.warning("**CAUTION:** Moderate risk. Set rigorous weekly limits and turn on 'Night Purchase' alerts.")
    elif simulated_risk > 25:
        st.info("**GOOD:** Fair risk control. Monitor weekend leisure expenses and maintain current trends.")
    else:
        st.success("**EXCELLENT:** Low risk. No immediate action required besides periodic tracking.")

with tab3:
    st.subheader("💸 Live Transaction Impulse Predictor")
    st.write("Enter details of a new transaction to check the impulse probability.")
    
    with st.form("predictor_form"):
        f_amount = st.number_input("Transaction Amount ($)", min_value=1.0, value=500.0)
        f_cat = st.selectbox("Category", ["Food", "Fashion", "Electronics", "Travel", "Grocery", "Entertainment", "Bills"])
        f_hour = st.slider("Hour of Day", 0, 23, 22)
        f_gap = st.checkbox("Short time since last purchase?")
        f_month_end = st.checkbox("Is it after the 25th of the month?")
        
        submit = st.form_submit_button("Predict Impulse Probablity")
        
    if submit:
        # Logic from generate_data.py
        is_night = 1 if f_hour >= 20 or f_hour <= 2 else 0
        is_discretionary = 1 if f_cat in ["Fashion", "Entertainment", "Electronics"] else 0
        is_spike = 1 if f_amount > (user_data["avg_amount"] / 15) else 0
        
        score = is_spike + is_night + is_discretionary + int(f_gap) + int(f_month_end)
        prob = (score / 5) * 100
        
        st.write(f"### Result: {prob:.0f}% Impulse Probability")
        st.progress(prob / 100)
        
        if score >= 3:
            st.error("🚩 This transaction is likely an **Impulse Purchase**.")
        else:
            st.success("💎 This looks like a **Planned Purchase**.")
        
        with st.expander("Why this result?"):
            st.write(f"- Night Transaction: {'Yes' if is_night else 'No'}")
            st.write(f"- Discretionary Category: {'Yes' if is_discretionary else 'No'}")
            st.write(f"- Spending Spike: {'Yes' if is_spike else 'No'}")
            st.write(f"- Short Time Gap: {'Yes' if f_gap else 'No'}")
            st.write(f"- End of Month: {'Yes' if f_month_end else 'No'}")
