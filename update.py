import streamlit as st
import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models

# Load data
data = 'punk'  # Gantilah "data.csv" dengan nama file data Anda

# Preprocessing data (misalnya: tokenisasi, stop words removal, stemming, dll.)

# Membangun corpus dan dictionary
text_data = data['text'].tolist()
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]

# Membangun model LDA
num_topics = st.sidebar.slider("Jumlah Topik", min_value=2, max_value=20, value=5)
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

# Tampilkan topik
st.sidebar.subheader("Topik Utama")
for topic in range(num_topics):
    st.sidebar.write(f"Topik {topic + 1}: {lda_model.print_topic(topic)}")

# Visualisasi dengan pyLDAvis
vis_data = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)
st.write("Visualisasi Topik:")
st.pydeck_chart(vis_data)

# Tampilkan dokumen dan topik yang relevan
st.sidebar.subheader("Analisis Dokumen")
document_index = st.sidebar.number_input("Nomor Dokumen (0 - 999)", min_value=0, max_value=len(data) - 1)
document = text_data[document_index]
document_bow = dictionary.doc2bow(document)
document_topics = lda_model.get_document_topics(document_bow)

st.write(f"Dokumen #{document_index}:")
st.write(data['text'][document_index])

st.write("Topik yang relevan:")
for topic, score in document_topics:
    st.write(f"Topik {topic + 1}: {score:.2f}")
