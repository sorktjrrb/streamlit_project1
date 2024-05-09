import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from prophet import Prophet

def run_graph():
    prophet = Prophet()
    df = pd.read_csv('./data/msft_stock_data.csv')

    df_prophet = df[['Date','Adj Close']]
    df_prophet.columns = ['ds', 'y']
    # print(df_prophet.columns)

    prophet.fit(df_prophet)
    
    st.markdown("<h2 style='text-align: center; color: black;'>< 시간에 따른 가격 예측 ></h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'><strong>원하는 기간을 입력해 주시면 시간에 따른 가격을 예측해 드립니다.</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'><strong>예측에는 Prophet 라이브러리를 활용하였습니다.</strong></p>", unsafe_allow_html=True)
    st.warning('기간은 1일 ~ 365일까지 입력 가능 합니다.')

    period = st.number_input('기간', min_value=1, max_value=365, value=1)

    future = prophet.make_future_dataframe(period, freq='B')
    forecast = prophet.predict(future)

    # print(forecast.info())

    st.dataframe(forecast)
    st.info('ds는 날짜별 데이터를 뜻하며 최종 예측한 값은 표의 가장 우측 yhat값을 참고하시면 됩니다.')

    st.markdown("<h2 style='text-align: center; color: black;'>Prophet 예측 결과 차트</h2>", unsafe_allow_html=True)
    
    # 예측 결과 플로팅
    fig1 = prophet.plot(forecast)
    st.pyplot(fig1)

    # 컴포넌츠 차트 플로팅
    fig2 = prophet.plot_components(forecast)
    st.pyplot(fig2)

    st.info('시계열 데이터 분석 결과 날짜가 지날수록 주식가격이 상승되는것을 확인할수 있습니다.')