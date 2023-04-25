# This is a sample Python script.
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
data = pd.read_csv('path/to/transaction_data.csv')
# Set the default plot to show transaction amount vs. time
st.title('PhonePe Pulse Dashboard')
st.subheader('Transaction Amount vs. Time')
fig = px.scatter(data, x='timestamp', y='transaction_amount')
st.plotly_chart(fig)
# Allow the user to filter the data by transaction type
st.subheader('Transaction Amount Distribution')
transaction_types = data['transaction_type'].unique()
selected_transaction_types = st.multiselect('Select transaction types', transaction_types)
filtered_data = data[data['transaction_type'].isin(selected_transaction_types)]

# Create a histogram of transaction amounts
fig = px.histogram(filtered_data, x='transaction_amount', nbins=50)
st.plotly_chart(fig)


