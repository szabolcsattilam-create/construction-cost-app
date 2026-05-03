import streamlit as st
import os

st.title("PDF Upload Tool")

# Create upload area
uploaded_file = st.file_uploader("Upload a floor plan (PDF)", type="pdf")

# If user uploads a file
if uploaded_file is not None:
    # Show file info
    st.write("File uploaded:", uploaded_file.name)

    # Create a folder to save files
    save_folder = "uploaded_pdfs"
    os.makedirs(save_folder, exist_ok=True)

    # Define file path
    file_path = os.path.join(save_folder, uploaded_file.name)

    # Save the file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File saved to {file_path}")