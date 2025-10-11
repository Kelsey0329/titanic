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

# Navigation button
st.subheader("Get Started")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Go to Main App", type="primary", use_container_width=True):
        st.switch_page("pages/app.py")

st.markdown("---")
st.markdown("*Built with Streamlit and powered by machine learning*")
