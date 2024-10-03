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
    
    # Create sliders for each column
    st.write("Rate the importance of each column (1 to 5):")
    for column in data.columns:
        slider_value = st.slider(column, 1, 5, 3)  # Default value is 3
        st.write(f"Importance rating for '{column}': {slider_value}")
