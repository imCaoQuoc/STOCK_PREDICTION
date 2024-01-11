import pandas as pd
import numpy as np
import tensorflow as tf
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

# Load pre-trained model
model = tf.keras.models.load_model("model_predict_stock.h5", compile=False)

def create_demo():
    #title của web
    st.title("STOCK PREDICTION")
    st.markdown('<h3 style="color: red"> USING LSTM </h3', unsafe_allow_html=True)
    
    #khung cung cấp thông tin để dự đoán
    st.sidebar.text("Enter Your Stock Information")

def enter_stock_symbol():
    #biến ticker để cập nhật theo mã cổ phiếu
    ticker = 0

    #mã cổ phiếu
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol")
    if stock_symbol:
        #nếu mã là FPT thì set ticker = 0 tương ứng FPT khi encode (coi file stock-prediction-finpros.ipynb)
        if stock_symbol == "FPT" or stock_symbol =="fpt":
            ticker = 0

        #nếu mã là MSN thì set ticker = 1 tương ứng MSN khi encode
        elif stock_symbol == "MSN" or stock_symbol == "msn":
            ticker = 1

        #nếu mã là PNJ thì set ticker = 2 tương ứng PNJ khi encode    
        elif stock_symbol == "PNJ" or stock_symbol == "PNJ":
            ticker = 2

        #nếu mã là VIN thì set ticker = 3 tương ứng VIC khi encode
        elif stock_symbol == "VIC" or stock_symbol == "vic":
            ticker = 3

        #nếu mã khác ngoài 4 mã trên, hiển thị là không có dữ liệu về mã cần dự đoán    
        else:
            st.text(f"Sorry, we don't have data about {stock_symbol}")
    st.sidebar.markdown("---")
    return stock_symbol, ticker

def enter_price():
    #giá mở cửa
    open_price = st.sidebar.number_input("Enter the price at the time of market opening")

    #giá trần
    high_price = st.sidebar.number_input("Enter the high price of stock")

    #giá sàn
    low_price = st.sidebar.number_input("Enter the low price")

    st.sidebar.markdown("---")
    return open_price , high_price, low_price

def enter_other_infor():
    #giá hiện tại
    present_price = st.sidebar.number_input("Enter the present price")

    #khối lượng khớp lệnh
    volume = st.sidebar.number_input("Enter the volume at present")

    st.sidebar.markdown("---") 
    return present_price, volume

def enter_date():
    #ngày hiện tại
    present_date = st.sidebar.date_input("Chọn ngày hiện tại", datetime(2018, 3, 7))

    #ngày cần dự đoán
    wanted_day = st.sidebar.number_input("Bạn muốn dự đoán cổ phiếu sau bao nhiêu ngày ?")

    #tính ngày cần dự đoán
    day = present_date + timedelta(days= int(wanted_day))
    month = day.month
    date = day.day

    return wanted_day, month, date

def run_predict(stock_symbol, ticker, open_price, high_price, low_price, present_price, volume, wanted_day, month, date):
    scaler = MinMaxScaler()
    present_price_array = np.array(present_price)

    #tạo input đầu vào cho model
    data_input = {"Ticker": [ticker], "Open": [open_price], "High": [high_price], "Low": [low_price], "Volume": [volume], "Month": [month], "Day": [date]}
    input = pd.DataFrame(data=data_input)
    input = scaler.fit_transform(input)
    price_true = scaler.fit_transform(present_price_array.reshape(-1, 1))

    #reshape về đúng dạng yêu cầu
    input= input.reshape(input.shape[0],1,7)

    #dự đoán giá cổ phiếu
    output_scaled_predict = model.predict(input)
    output = scaler.inverse_transform(output_scaled_predict)
    chenh_lech_gia = output[0][0] - present_price
    #hiện kết quả
    st.text(f"Giá dự đoán của cổ phiếu {stock_symbol} sau {int(wanted_day)} ngày là {output[0][0]}")
    st.text(f"Biến động giá cổ phiếu so với hiện tại là {chenh_lech_gia}")

if __name__ == '__main__':

    create_demo()
    stock_symbol, ticker = enter_stock_symbol()
    open_price, high_price, low_price = enter_price()
    present_price, volume = enter_other_infor()
    wanted_day, month, date = enter_date()

    start = st.sidebar.button("PREDICT")
    if start: 
        run_predict(stock_symbol, ticker, open_price, high_price, low_price, present_price ,volume, wanted_day, month, date)
        st.markdown("---")