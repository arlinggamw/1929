import streamlit as st
import pickle
import numpy as np

# Muat model ML Anda (di sini menggunakan contoh Regresi Linear)
#model = pickle.load(open('model.pkl', 'rb'))

st.title('Aplikasi Deployment Model ML dengan Streamlit')

# Masukkan fitur yang diperlukan
feature1 = st.slider('Feature 1', 0.0, 100.0, 0.0)
feature2 = st.slider('Feature 2', 0.0, 100.0, 0.0)

# Prediksi dengan model
input_features = np.array([feature1, feature2]).reshape(1, -1)
#prediction = model.predict(input_features)

#st.write('Hasil Prediksi:', prediction[0])
st.write('mantap')
