import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
with open("slang.txt", "r") as file:
        slang_words = file.read()

#fungsi cleaning
def cleaning_text(text):
  temp = re.sub(r'\<.*?\>', ' ', text)
  temp = re.sub('/n', ' ', temp)
  temp = temp.lower()
  temp = re.sub("[^a-z0-9]"," ", temp)
  #remove number
  temp = re.sub(r'\d+', '',text)
  #normalisasi teks
  temp = temp.split()
  for w in temp:
    if w in slang_words.keys():
       temp[temp.index(w)] = slang_words[w]
  temp = " ".join(word for word in temp)
  temp = stopword.remove(temp)
  #stemming teks
  temp = stemmer.stem(temp)
  temp = temp.replace("nbsp", "")
  temp = temp.replace("image", "")
  temp = temp.replace("attach", "")
  temp = temp.replace("png", "")
  temp = temp.replace("call", "")
  temp = temp.replace("center", "")
  temp = temp.replace("kpp", "")
  temp = temp.replace("pratama", "")
  temp = temp.replace("tanggal", "")
  temp = temp.replace("januari", "")
  temp = temp.replace("februari", "")
  temp = temp.replace("maret", "")
  temp = temp.replace("april", "")
  temp = temp.replace(" mei ", " ")
  temp = temp.replace("juni", "")
  temp = temp.replace("juli", "")
  temp = temp.replace("agustus", "")
  temp = temp.replace("september", "")
  temp = temp.replace("oktober", "")
  temp = temp.replace("november", "")
  temp = temp.replace("desember", "")
  temp = temp.replace("kantor", "")
  temp = temp.replace(" nip ", " ")
  temp = temp.replace("nrp", "")
  temp = temp.replace("wilayah", "")
  temp = temp.replace("kppn", "")
  temp = temp.replace("kepala", "")
  temp = temp.replace("seksi", "")
  temp = temp.replace("email", "")
  temp = temp.replace("hai", "")
  temp = temp.replace("djpb", "")
  temp = temp.replace("selamat", "")
  temp = temp.replace("pagi", "")
  temp = temp.replace("siang", "")
  temp = temp.replace("sore", "")
  temp = temp.replace("malam", "")
  temp = temp.replace("nik ", "")
  temp = temp.replace("nip ", "")
  temp = temp.replace("live", "")
  temp = temp.replace("chat", "")
  return temp

#fungsi input pertanyaan
def pertanyaan_baru(text):
  user_input = cleaning_text(text)
  user_vector = vectorizer.transform([user_input])
  similarities = cosine_similarity(user_vector, question_vectors)
  if similarities.max() > 0.5:
    # Find the index of the most similar question
    jawab = dataset.jawab_clean[similarities.argmax()]
  else:
    jawab = "Pertanyaan anda akan diteruskan ke agen Hai DJPb"
    
  return jawab




dataset = pd.read_excel("data_git.xlsx")
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(dataset.tanya_clean)


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

st.write("Anda memasukkan:", pertanyaan_baru(user_input))

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
