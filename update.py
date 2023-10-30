import streamlit as st


# Judul Aplikasi
st.title("MockUp Aplikasi ANAK AYAM")

# Deskripsi Aplikasi
st.markdown("Selamat datang di aplikasi ANAK AYAM ini. Ini adalah contoh antarmuka sederhana tanpa menggunakan pustaka eksternal.")

# Teks Sambutan
st.header("Selamat Datang di ANAK AYAM")
st.write("Aplikasi ini dibuat dengan menggunakan Streamlit, yang memungkinkan Anda untuk membuat aplikasi web dengan mudah.")

# Gambar
st.image("ANAK AYAM LOGO BLUE.jpg", caption="ANAK AYAM JAYA JAYA JAYA!!!!!")

# Grafik
st.subheader("Grafik Contoh")
st.line_chart({"Data 1": [1, 2, 3, 4, 5],
              "Data 2": [5, 4, 3, 2, 1]})

# Input Pengguna
user_input = st.text_input("Masukkan sesuatu:")
st.write("Anda memasukkan:", user_input)

# Tombol
if st.button("Klik di sini"):
    st.write("Anda menekan tombol!")

# Pilihan
options = ["P Gelud", "gas bang", "lalala","9999+"]
selected_option = st.selectbox("Jangan diklik:", options)
st.write("Anda memilih:", selected_option)

# Sidebar
st.sidebar.header("Tentang Aplikasi")
sidebar_style = """
    <style>
        .css-1l02z5r {
            background-color: #3498db;
        }
    </style>
"""

st.markdown(sidebar_style, unsafe_allow_html=True)

st.sidebar.markdown("Ini adalah aplikasi Streamlit sederhana tanpa pustaka eksternal.")

# Tampilkan teks berformat
st.markdown("**Ini adalah teks berformat**. *Ini adalah teks miring*.")

# Hyperlink
st.markdown("Baca lebih lanjut di [dokumentasi Streamlit](https://streamlit.io/docs/).")
