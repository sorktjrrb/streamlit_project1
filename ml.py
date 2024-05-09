import streamlit as st
import joblib
import numpy as np
import math
import pandas as pd
import datetime

def run_ml():

    st.subheader("주식 가격 예측하기")
    st.info('Prophet을 통해 예측한 결과 날짜 데이터도 유효한것으로 확인되어 머신러닝에는 time 이라는 변수로 수치화해 일자가 지날수록 데이터값이 1씩 증가하도록하여 학습하였습니다.')
    st.info('날짜값을 확인하신후 수치로 입력후, 시가, 최고가, 최저가, 마감가, 거래량을 예측하여 입력하셔야 합니다. 예측을 원하시는 날짜와 가장 가까운날짜를 기반으로 실제데이터값과 유사하게 예측값을 입력하시는게 좋습니다.')
    st.link_button('이전 주식 데이터 확인',url='https://kr.investing.com/equities/microsoft-corp-historical-data')
    st.warning('주식 데이터의 경우 변동성이 심해 정확한 예측이 어렵습니다. 대략적인 시장의 크기나 매출에 대해 시간에 따른 추세정도로만 참고해주세요.')

    data = {
    'Date': pd.date_range(start='2010-01-04', end='2025-12-31', freq='B'),
    'time': range(1, 4174)
    }
    df_date = pd.DataFrame(data)
    df_date['Date'] = df_date['Date'].apply(lambda x: x.date())

    # Streamlit 앱 생성
    st.subheader('Time 값 조회 앱')
    st.info('날짜값(time)은 2010-01-04 부터 2025-12-31일까지만 조회가능합니다.')

    # 사용자가 날짜를 선택할 수 있는 date picker 추가
    selected_date = st.date_input('날짜를 선택하세요', value=pd.to_datetime('2024-12-31'))
    # print(type(selected_date))

    # 선택된 날짜에 해당하는 time 값을 찾아서 출력
    selected_time = df_date.loc[df_date['Date'] == selected_date, 'time'].values
    if len(selected_time) > 0:
        st.success(f'선택한 날짜의 time 값은 {selected_time[0]} 입니다.')
        time = st.number_input('선택하신 날짜값(time)이 자동으로 입력됩니다', selected_time[0])
    else:
        st.error('해당하는 데이터가 없습니다. 유요한 기간내에 평일을 기준으로 선택해주세요.')

    # 'time','Open','High','Low','Close','Volume' 데이터 입력 순서

    st.text('예측되는 시가를 수치로 입력하세요')
    open = st.number_input('시가', min_value=0, max_value=1000, value=350)

    st.text('예측되는 최고가를 수치로 입력하세요')
    high = st.number_input('최고가', min_value=0, max_value=1000, value=350)

    st.text('예측되는 최저가를 수치로 입력하세요')
    low = st.number_input('최저가', min_value=0, max_value=1000, value=350)

    st.text('예측되는 마감가를 수치로 입력하세요')
    close = st.number_input('마감가', min_value=0, max_value=1000, value=350)

    st.text('예측되는 거래량을 수치로 입력하세요')
    volume = st.number_input('거래량', min_value=0, max_value=100000000, value=25000000, step=1000000)

    st.subheader('버튼을 누르면 최종 마감 가격을 예측합니다.')

    if st.button('예측하기') :

        # 2-1. 모델이 있어야 한다.
        regressor = joblib.load('./model/regressor.pkl')
        print(regressor)

        # 2-2. 유저가 입력한 데이터를, 모델에 예측할수 있도록 가공해야 한다.
        new_data = [time, open, high, low, close, volume]
        print(new_data)
        new_data = np.array(new_data).reshape(1, 6)

        # 2-3. 모델의 predict 함수로 예측한다.
        y_pred = regressor.predict(new_data)
        
        # 1. y_pred 에서 숫자만 가져온다.
        y_pred = y_pred[0]
        print(y_pred)

        # 2. 숫자의 소수점 뒤 제거
        y_pred = round(y_pred)
        print(y_pred)

        st.success(f'위의 데이터로 예측한 주식 최종 종가는 ${y_pred} 입니다.')