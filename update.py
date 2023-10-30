
# Judul Aplikasi
st.title("Analisis Topic Modeling dengan Streamlit")

# Sidebar
st.sidebar.subheader("Pengaturan")
num_topics = st.sidebar.slider("Jumlah Topik", min_value=2, max_value=20, value=5)

# Upload Dataset
st.sidebar.subheader("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Pilih file CSV", type=["csv"])

if uploaded_file is not None:
    data = 'punk'

    # Data Preprocessing (tokenisasi, stop words removal, dll.)

    # Membangun corpus dan dictionary
    text_data = data['text'].tolist()
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    # Membangun model LDA
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

    # Visualisasi dengan pyLDAvis
    vis_data = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)

    # Tampilkan Visualisasi Topik
    st.write("Visualisasi Topik:")
    st.pydeck_chart(vis_data)

    # Pilihan Topik
    st.sidebar.subheader("Pilihan Topik")
    selected_topic = st.sidebar.selectbox("Pilih Topik", range(num_topics))

    # Tampilkan Dokumen dalam Topik yang Dipilih
    st.write(f"Topik yang Dipilih: Topik {selected_topic + 1}")
    st.subheader("Dokumen dalam Topik yang Dipilih:")
    documents_in_topic = [i for i, topics in enumerate(lda_model.get_document_topics(corpus)) if selected_topic in [topic[0] for topic in topics]]
    for doc_index in documents_in_topic:
        st.write(f"Dokumen #{doc_index + 1}:")
        st.write(data['text'][doc_index])
else:
    st.write("Silakan unggah dataset untuk memulai analisis topic modeling.")
