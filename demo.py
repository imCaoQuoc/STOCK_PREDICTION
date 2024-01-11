import pandas as pd
import tensorflow
import streamlit as st
from datetime import datetime, timedelta

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
    date = st.date_input("Chọn ngày hiện tại", datetime(2019, 7, 6))
    day = st.number_input("Bạn muốn dự đoán cổ phiếu sau bao nhiêu ngày ?")
    start = st.sidebar.button("PREDICT")
    if start: 
        data_input = {"Ticker": [ticker], "Open": [open_price], "High": [high_price], "Low": [low_price], "Volume": [volume]}
        input = pd.DataFrame(data=data_input)
        input= input.values.reshape(input.shape[0],1,5)
        output = model.predict(input)
        st.text(f"Gía dự đoán của cổ phiếu {stock_symbol} trong tương lai là {output[0][0]}")
        st.text(f"Biến động giá cổ phiếu so với hiện tại là {output[0][0] - present_price}")

        st.markdown("---")
        # Tách giá trị năm, tháng, ngày
        nam = date.year
        thang = date.month
        ngay = date.day

        # In kết quả
        st.text(f"Năm: {nam}")
        st.text(f"Tháng: {thang}")
        st.text(f"Ngày: {ngay}")
        st.markdown("---")
        # Tính toán ngày 10 ngày sau
        ngay_10_ngay_sau = date + timedelta(days= int(day))
        nam2 = ngay_10_ngay_sau.year
        thang2 = ngay_10_ngay_sau.month
        ngay2 = ngay_10_ngay_sau.day

        # In kết quả
        st.text(f"Năm: {nam2}")
        st.text(f"Tháng: {thang2}")
        st.text(f"Ngày: {ngay2}")
        
    

