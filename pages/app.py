import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply seaborn style
sns.set_style("darkgrid")

# Set page configuration
st.set_page_config(
    page_title="Titanic - Main App",
    page_icon="🚢",
    layout="wide"
)

# Display page title
st.title("Titanic App by Xirui Hu")

# Read the train.csv file
df = pd.read_csv("train.csv")

# Display the entire dataframe
st.subheader("Titanic Dataset")
st.dataframe(df)

# Create three side-by-side box plots
st.subheader("Fare Distribution by Passenger Class")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Box plot for Pclass 1
pclass_1 = df[df['Pclass'] == 1]['Fare']
axes[0].boxplot(pclass_1.dropna())
axes[0].set_xlabel('Passenger Class 1')
axes[0].set_ylabel('Fare')

# Box plot for Pclass 2
pclass_2 = df[df['Pclass'] == 2]['Fare']
axes[1].boxplot(pclass_2.dropna())
axes[1].set_xlabel('Passenger Class 2')
axes[1].set_ylabel('Fare')

# Box plot for Pclass 3
pclass_3 = df[df['Pclass'] == 3]['Fare']
axes[2].boxplot(pclass_3.dropna())
axes[2].set_xlabel('Passenger Class 3')
axes[2].set_ylabel('Fare')

# Display the figure in Streamlit
st.pyplot(fig)

if st.button("← Back to Home"):
    st.switch_page("home.py")
