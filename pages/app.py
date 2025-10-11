import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Titanic - Main App",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Titanic Data Analysis and Prediction")

st.markdown("""
### Main Application

This is the main Titanic application page.

*Note: Full functionality will be implemented in subsequent tasks.*
""")

if st.button("← Back to Home"):
    st.switch_page("home.py")
