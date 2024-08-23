import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Sidebar
st.title('Solar Radiation Data Dashboard')
st.sidebar.header('User Input Parameters')

# Load Data (you may dynamically fetch or load from a file)
@st.cache
def load_data():
    # Example: Load a CSV file
   return pd.read_csv(r'C:\Users\Naim\solar_radition\data\benin-malanville.csv')


data = load_data()

# Example of User Inputs
st.sidebar.subheader('Time Period')
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')

# Filter data based on user input
filtered_data = data[(data['Timestamp'] >= pd.to_datetime(start_date)) & (data['Timestamp'] <= pd.to_datetime(end_date))]

# Example Plot
st.subheader('GHI Over Time')
fig, ax = plt.subplots()
ax.plot(filtered_data['Timestamp'], filtered_data['GHI'], label='GHI')
ax.set_xlabel('Timestamp')
ax.set_ylabel('GHI')
ax.legend()
st.pyplot(fig)

# Example: Displaying the Data
st.write('Data Snapshot')
st.write(filtered_data.head())
