import numpy as np
import tensorflow
import streamlit as st

# Load pre-trained model
model = tensorflow.keras.models.load_model("model_predict_stock.h5", compile=False)
st.title("STOCK PREDICTION")
st.markdown('<h3 style="color: red"> USING LSTM </h3', unsafe_allow_html=True)


st.sidebar.text('Input data')
