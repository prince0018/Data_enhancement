import streamlit as st
import pandas as pd

# Set the title for the second page
st.title("Upload Your Dataset")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    
    # Display the contents of the dataframe
    st.write("Here is the content of your dataset:")
    st.dataframe(data)  # Display the dataframe in an interactive table
