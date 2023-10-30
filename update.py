import streamlit as st

# Judul Aplikasi
st.title("Aplikasi Streamlit Menarik Tanpa Instalasi Pustaka")

# Deskripsi Aplikasi
st.markdown("Selamat datang di aplikasi Streamlit ini. Ini adalah contoh antarmuka sederhana tanpa menggunakan pustaka eksternal.")

# Teks Sambutan
st.header("Selamat Datang di Aplikasi Streamlit")
st.write("Aplikasi ini dibuat dengan menggunakan Streamlit, yang memungkinkan Anda untuk membuat aplikasi web dengan mudah.")

# Gambar
st.image("isleworth-mona-lisa.jpg", caption="Ini adalah gambar monalisa")

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
options = ["Pilihan 1", "Pilihan 2", "Pilihan 3"]
selected_option = st.selectbox("Pilih sesuatu:", options)
st.write("Anda memilih:", selected_option)

# Sidebar
st.sidebar.header("Tentang Aplikasi")
st.sidebar.markdown("Ini adalah aplikasi Streamlit sederhana tanpa pustaka eksternal.")

# Tampilkan teks berformat
st.markdown("**Ini adalah teks berformat**. *Ini adalah teks miring*.")

# Hyperlink
st.markdown("Baca lebih lanjut di [dokumentasi Streamlit](https://streamlit.io/docs/).")
