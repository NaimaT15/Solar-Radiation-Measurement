import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Sidebar
st.title('Solar Radiation Data Dashboard')
st.sidebar.header('User Input Parameters')

# Load Data (you may dynamically fetch or load from a file)
@st.cache_data
def load_data():
    # Load CSV files for each region
    benin = pd.read_csv(r'C:\Users\Naim\solar_radition\data\benin-malanville.csv')
    sierraleone = pd.read_csv(r'C:\Users\Naim\solar_radition\data\sierraleone-bumbuna.csv')
    togo = pd.read_csv(r'C:\Users\Naim\solar_radition\data\togo-malanville.csv')
    
    # Return as a dictionary
    return {'Benin-Malanville': benin, 'Sierraleone-Bumbuna': sierraleone, 'Togo-Malanville': togo}

data_dict = load_data()

# Sidebar selection for region
st.sidebar.subheader('Region')
region_selected = st.sidebar.selectbox('Select Region', options=list(data_dict.keys()))

# Sidebar input for time period
st.sidebar.subheader('Time Period')
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')

# Convert start_date and end_date to pandas Timestamp
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data based on selected region and user input dates
data = data_dict[region_selected]
filtered_data = data[(pd.to_datetime(data['Timestamp']) >= start_date) & (pd.to_datetime(data['Timestamp']) <= end_date)]

# Plot for GHI over time
st.subheader(f'GHI Over Time - {region_selected}')
fig, ax = plt.subplots()
ax.plot(filtered_data['Timestamp'], filtered_data['GHI'], label='GHI')
ax.set_xlabel('Timestamp')
ax.set_ylabel('GHI')
ax.legend()
st.pyplot(fig)

# Display the Data
st.write(f'Data Snapshot for {region_selected}')
st.write(filtered_data.head())
