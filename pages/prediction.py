import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Titanic - Prediction",
    page_icon="🚢",
    layout="wide"
)

# Display page title
st.title("Titanic Survival Prediction")
st.markdown("Predict the survival probability of a Titanic passenger based on their information.")

# Load the trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("titanic_model.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is not None:
    # Create input form
    st.subheader("Enter Passenger Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Passenger Class input
        pclass = st.selectbox(
            "Passenger Class",
            options=[1, 2, 3],
            index=1,  # Default to 2
            help="1 = First Class, 2 = Second Class, 3 = Third Class"
        )
        
        # Sex input
        sex = st.selectbox(
            "Sex",
            options=["male", "female"],
            index=0,  # Default to male
            help="Select passenger's sex"
        )
    
    with col2:
        # Age input
        age = st.number_input(
            "Age",
            min_value=0.0,
            max_value=100.0,
            value=24.0,  # Default to 24
            step=1.0,
            help="Passenger's age in years"
        )
        
        # Fare input
        fare = st.number_input(
            "Fare",
            min_value=0.0,
            max_value=600.0,
            value=32.0,  # Default to 32
            step=0.1,
            help="Ticket fare in pounds"
        )
    
    # Predict button
    if st.button("Predict Survival", type="primary", use_container_width=True):
        # Encode sex (male=1, female=0)
        sex_encoded = 1 if sex == "male" else 0
        
        # Create input array with feature names
        input_data = pd.DataFrame({
            'Pclass': [pclass],
            'Sex': [sex_encoded],
            'Age': [age],
            'Fare': [fare]
        })
        
        try:
            # Get prediction probability
            proba = model.predict_proba(input_data)
            survival_prob = proba[0][1]
            death_prob = proba[0][0]
            
            # Display results
            st.markdown("---")
            st.subheader("Prediction Results")
            
            # Display probability with color-coded message
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    label="Survival Probability",
                    value=f"{survival_prob:.2%}",
                    delta=None
                )
            
            with col2:
                st.metric(
                    label="Death Probability",
                    value=f"{death_prob:.2%}",
                    delta=None
                )
            
            # Display interpretation
            st.markdown("### Interpretation")
            if survival_prob > 0.5:
                st.success(f"✅ This passenger has a **{survival_prob:.2%}** chance of survival. The model predicts they would likely **survive**.")
            else:
                st.error(f"❌ This passenger has a **{survival_prob:.2%}** chance of survival. The model predicts they would likely **not survive**.")
            
            # Display input summary
            st.markdown("### Input Summary")
            st.write(f"- **Passenger Class:** {pclass}")
            st.write(f"- **Sex:** {sex}")
            st.write(f"- **Age:** {age} years")
            st.write(f"- **Fare:** £{fare:.2f}")
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            import traceback
            st.code(traceback.format_exc())

# Navigation button
st.markdown("---")
if st.button("← Back to Home"):
    st.switch_page("home.py")
