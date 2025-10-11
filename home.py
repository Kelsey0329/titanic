import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Titanic - Home",
    page_icon="🚢",
    layout="wide"
)

# Title and welcome message
st.title("🚢 Welcome to the Titanic Data Analysis App")

st.markdown("""
### About This Application

This application provides data analysis and predictions using the famous Titanic dataset.

The Titanic dataset contains information about passengers aboard the Titanic, including:
- Passenger details (name, age, sex, class)
- Family information (siblings/spouses, parents/children)
- Ticket and fare information
- Survival status

Use this app to:
- Explore the Titanic dataset
- Visualize passenger statistics
- Make survival predictions using machine learning

---
""")

# Navigation buttons
st.subheader("Get Started")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Data Analysis", use_container_width=True):
        st.switch_page("pages/app.py")

with col2:
    if st.button("🔮 Survival Prediction", type="primary", use_container_width=True):
        st.switch_page("pages/prediction.py")

with col3:
    st.empty()  # Placeholder for future features

st.markdown("---")
st.markdown("*Built with Streamlit and powered by machine learning*")
from data_analysis import show_data_analysis
from prediction import show_prediction

