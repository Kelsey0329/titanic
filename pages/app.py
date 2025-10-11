import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np
import warnings

# Suppress sklearn version warning
warnings.filterwarnings('ignore', category=UserWarning)

# Set page configuration
st.set_page_config(
    page_title="Titanic - Main App",
    page_icon="🚢",
    layout="wide"
)

# Apply seaborn style
sns.set_style("whitegrid")

st.title("🚢 Titanic App by Xirui Hu")

# Create tabs for different sections
tab1, tab2 = st.tabs(["📊 Data Analysis", "🔮 Survival Prediction"])

# Tab 1: Data Analysis
with tab1:
    st.header("Data Analysis")
    
    # Read and display the dataframe
    df = pd.read_csv('train.csv')
    st.subheader("Titanic Dataset")
    st.dataframe(df)
    
    # Create box plots
    st.subheader("Fare Distribution by Passenger Class")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, pclass in enumerate([1, 2, 3]):
        class_data = df[df['Pclass'] == pclass]['Fare']
        axes[idx].boxplot(class_data.dropna(), widths=0.5)
        axes[idx].set_xlabel(f'Class {pclass}')
        axes[idx].set_ylabel('Fare')
        axes[idx].set_title(f'Passenger Class {pclass}')
    
    plt.tight_layout()
    st.pyplot(fig)

# Tab 2: Prediction
with tab2:
    st.header("Survival Prediction")
    st.markdown("Enter passenger information to predict survival probability:")
    
    # Load the model
    @st.cache_resource
    def load_model():
        return joblib.load('titanic_model.pkl')
    
    model = load_model()
    
    # Create input widgets
    col1, col2 = st.columns(2)
    
    with col1:
        pclass = st.selectbox("Passenger Class", [1, 2, 3], index=1)
        sex = st.selectbox("Sex", ["male", "female"])
    
    with col2:
        age = st.number_input("Age", min_value=0.0, max_value=100.0, value=24.0, step=1.0)
        fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0, step=0.1)
    
    # Predict button
    if st.button("Predict Survival Probability", type="primary"):
        # Encode sex: male=1, female=0
        sex_encoded = 1 if sex == "male" else 0
        
        # Prepare input data
        input_data = np.array([[pclass, sex_encoded, age, fare]])
        
        # Make prediction
        proba = model.predict_proba(input_data)
        survival_prob = proba[0][1]
        
        # Display result
        st.success(f"### Survival Probability: {survival_prob:.2%}")
        
        # Additional visualization
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Probability of Survival", f"{survival_prob:.2%}")
        with col2:
            st.metric("Probability of Not Surviving", f"{(1-survival_prob):.2%}")
        
        # Progress bar visualization
        st.write("Visual representation:")
        st.progress(survival_prob)
        
        if survival_prob > 0.5:
            st.info("💚 This passenger has a higher chance of survival.")
        else:
            st.warning("💔 This passenger has a lower chance of survival.")

# Back to home button
st.markdown("---")
if st.button("← Back to Home"):
    st.switch_page("home.py")
