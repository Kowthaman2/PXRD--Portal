import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="High Entropy Oxides Library", layout="wide")

# Define categories
categories = {
    "Rocksalt Combination Library": "rocksalt",
    "Fluorite-Type Library": "fluorite",
    "Perovskite-Type Library": "perovskite",
    "Spinel-Type Library": "spinel",
    "Other Structures": "other"
}

st.markdown("## 🧪 High Entropy Oxides Library")
st.markdown("Organize your PXRD uploads by structural type below.")

# Select category
structure_type = st.selectbox("Select Structure Type", list(categories.keys()))
folder_name = categories[structure_type]
UPLOAD_DIR = os.path.join("uploaded_files", folder_name)
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload file
st.markdown(f"### Upload to `{structure_type}`")
uploaded_file = st.file_uploader("Upload your PXRD file", type=["asc", "csv", "txt", "cif"], key=folder_name)
if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Uploaded to {structure_type}: {uploaded_file.name}")

# Show files per category
st.markdown("### 📂 Uploaded Files")
for display_name, folder in categories.items():
    full_path = os.path.join("uploaded_files", folder)
    st.markdown(f"**🔸 {display_name}**")
    if os.path.exists(full_path) and os.listdir(full_path):
        file_data = {
            "File Name": [],
            "Download Link": []
        }
        for file in os.listdir(full_path):
            file_data["File Name"].append(file)
            file_data["Download Link"].append(f"[📥 Download](./uploaded_files/{folder}/{file})")
        df = pd.DataFrame(file_data)
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.info("No files uploaded yet in this category.")
