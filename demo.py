import numpy as np
import tensorflow
import streamlit as st

# Load pre-trained model
model = tensorflow.keras.models.load_model("model_predict_stock.h5", compile=False)
ticker = 0

if __name__ == '__main__':
    st.title("STOCK PREDICTION")
    st.markdown('<h3 style="color: red"> USING LSTM </h3', unsafe_allow_html=True)
    st.sidebar.text("Your Stock Information")
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol")
    if stock_symbol == "FPT" or stock_symbol =="fpt":
        ticker = 0
    elif stock_symbol == "MSN" or stock_symbol == "msn":
        ticker = 1
    elif stock_symbol == "PNJ" or stock_symbol == "PNJ":
        ticker = 2
    elif stock_symbol == "VIN" or stock_symbol == "vin":
        ticker = 3
    else:
        st.text(f"Sorry, we don't have data about {stock_symbol}")
    st.sidebar.markdown("---")
    open_price = st.sidebar.number_input("Enter the price at the time of market opening")
    high_price = st.sidebar.number_input("Enter the high price of stock")
    low_price = st.sidebar.number_input("Enter the low price")
    st.sidebar.markdown("---")
    present_price = st.sidebar.number_input("Enter the present price")
    volume = st.sidebar.number_input("Enter the volume at present")

