import streamlit as st
import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models

# Judul Aplikasi
st.title("Aplikasi Analisis Topic Modeling")

# Sidebar
st.sidebar.subheader("Pengaturan")
num_topics = st.sidebar.slider("Jumlah Topik", min_value=2, max_value=20, value=5)

# Pilihan Dataset (contoh: pilihan statis)
dataset_option = st.sidebar.radio("Pilih Dataset", ["Dataset 1", "Dataset 2", "Dataset 3"])

# Visualisasi Topik (contoh: grafik statis)
st.sidebar.subheader("Visualisasi Topik")
st.sidebar.image("grafik_topik.png", use_container_width=True)

# Informasi Tambahan (contoh: teks statis)
st.sidebar.subheader("Informasi Topik")
st.sidebar.write("Topik Utama: Topik 1")
st.sidebar.write("Deskripsi: Ini adalah topik utama yang membahas topik-topik penting.")

# Data Mockup
data = pd.DataFrame({
    'Dokumen': range(1, 11),
    'Teks Dokumen': [
        "Ini adalah contoh dokumen 1.",
        "Ini adalah contoh dokumen 2.",
        "Ini adalah contoh dokumen 3.",
        "Ini adalah contoh dokumen 4.",
        "Ini adalah contoh dokumen 5.",
        "Ini adalah contoh dokumen 6.",
        "Ini adalah contoh dokumen 7.",
        "Ini adalah contoh dokumen 8.",
        "Ini adalah contoh dokumen 9.",
        "Ini adalah contoh dokumen 10."
    ]
})

# Tampilan Utama
st.subheader("Visualisasi Topik")
st.image("visualisasi_topik.png", use_container_width=True)

st.subheader("Daftar Dokumen")
st.dataframe(data, width=600, height=300)

selected_document = st.selectbox("Pilih Dokumen", data['Dokumen'])
document_text = data[data['Dokumen'] == selected_document]['Teks Dokumen'].values[0]

st.subheader("Analisis Dokumen")
st.write(f"Dokumen #{selected_document}:")
st.write(document_text)

st.write("Topik yang relevan:")
st.write("Topik 1: 0.75")
st.write("Topik 2: 0.20")
st.write("Topik 3: 0.05")

# Informasi Tambahan (contoh: teks statis)
st.sidebar.subheader("Tentang Aplikasi")
st.sidebar.write("Aplikasi ini digunakan untuk menganalisis topik dalam dataset teks menggunakan model Topic Modeling.")
