import numpy as np
import tensorflow
import streamlit as st

# Load pre-trained model
model = tensorflow.keras.models.load_model("model_predict_stock.h5", compile=False)
st.title("STOCK PREDICTION USING LSTM")

