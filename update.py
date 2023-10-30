import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Aplikasi Streamlit Sederhana")

# Pilihan Dataset
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    data = 'punk'

    # Tampilkan Dataset
    st.subheader("Data:")
    st.write(data)

    # Statistik Dataset
    st.subheader("Statistik Data:")
    st.write(data.describe())
else:
    st.write("Silakan unggah dataset untuk memulai analisis.")
