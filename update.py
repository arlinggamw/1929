!pip install sklearn
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Fungsi untuk pemodelan topik
def run_lda(df, num_topics):
    vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    data_vectorized = vectorizer.fit_transform(df['text'])

    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(data_vectorized)

    return lda

# Tampilan Streamlit
st.title('Aplikasi Pemodelan Topik')

# Unggah dokumen
st.write('### Unggah Dokumen')
uploaded_file = st.file_uploader('Unggah file CSV yang berisi teks dokumen', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    num_topics = st.slider('Pilih Jumlah Topik', 2, 10, 4)

    if st.button('Mulai Pemodelan'):
        lda_model = run_lda(df, num_topics)
        st.success('Pemodelan selesai!')

        # Tampilkan kata-kata kunci untuk setiap topik
        st.write('### Kata-kata Kunci Topik:')
        for i, topic in enumerate(lda_model.components_):
            top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:][::-1]]
            st.write(f'Topik {i+1}: {", ".join(top_words)}')
