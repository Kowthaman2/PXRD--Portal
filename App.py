import streamlit as st
import os

# Create upload folder if it doesn't exist
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("📁 PXRD File Upload Portal")

# Upload section
uploaded_file = st.file_uploader("Upload PXRD or other files", type=["asc", "csv", "txt", "cif"])
if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Uploaded: {uploaded_file.name}")

# List uploaded files
st.subheader("📂 Uploaded Files")
files = os.listdir(UPLOAD_DIR)
if files:
    for file in files:
        st.markdown(f"[{file}](./{UPLOAD_DIR}/{file})")
else:
    st.info("No files uploaded yet.")
