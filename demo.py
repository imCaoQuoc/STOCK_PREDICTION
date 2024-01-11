import pandas as pd
import tensorflow
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

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

    start = st.sidebar.button("PREDICT")
    if start: 
        data_input = {"Ticker": [ticker], "Open": [open_price], "High": [high_price], "Low": [low_price], "Volume": [volume]}
        input = pd.DataFrame(data=data_input)
        scaler = MinMaxScaler()
        input = scaler.fit_transform(input)
        input_scaled = input.reshape(input.shape[0],1,5)
        output = model.predict(input_scaled)
        #output = scaler.inverse_transform(output_scaled.reshape(-1, 1))
        st.text(f"Gía dự đoán của cổ phiếu {stock_symbol} trong tương lai là {output}")
        st.text(f"Biến động giá cổ phiếu so với hiện tại là {output - present_price}")
    

