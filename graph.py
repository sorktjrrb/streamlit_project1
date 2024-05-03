import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from prophet import Prophet

def run_graph():
    prophet = Prophet()
    df = pd.read_csv('./data/msft_stock_data.csv')

    df_prophet = df[['Date','High']]
    df_prophet.columns = ['ds', 'y']
    print(df_prophet.columns)

    prophet.fit(df_prophet)
    future = prophet.make_future_dataframe(periods= 365, freq='B')

    st.markdown("<h2 style='text-align: center; color: black;'>Prophet 예측 결과</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'>Prophet을 이용하여 1년후에 주식가격까지 예측해 보았습니다.</p>", unsafe_allow_html=True)

    forecast = prophet.predict(future)

    print(forecast.info())

    st.write(forecast)

    st.markdown("<h2 style='text-align: center; color: black;'>Prophet 예측 결과 차트</h2>", unsafe_allow_html=True)
    st.image('./image/prophet1.png', use_column_width=True)
    st.image('./image/prophet2.png', use_column_width=True)

    st.info('시계열 데이터 분석 결과 날짜가 지날수록 주식가격이 상승되는것을 확인할수 있습니다.')