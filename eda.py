import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from prophet import Prophet

def run_eda() :
    st.markdown("<h2 style='text-align: center; color: black;'>탐색적 데이터 분석</h2>", unsafe_allow_html=True)

    df = pd.read_csv('./data/df_v1.csv')

    print(df)

    radio_menu = ['데이터프레임', '통계치']

    choice_radio = st.radio('데이터프레임 보기 / 통계치 보기를 할 수 있습니다.', radio_menu)

    if choice_radio == radio_menu[0] :
        st.dataframe(df)
    elif choice_radio == radio_menu[1] :
        st.dataframe(df.describe())

    # '날짜', '시가', '최고가', '최저가', '종가', '마감가', '거래량',
    # 날짜데이터를 prophet로 유의미한걸 보여주고 time값으로 수치화할 예정

    st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 보여드립니다.')
    column_list = ['시가', '최고가', '최저가', '종가', '마감가', '거래량']
    choice_column = st.selectbox('컬럼을 선택하세요.', column_list)

    st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
    st.dataframe( df.loc[df[choice_column] == df[choice_column].max(), ])

    st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
    st.dataframe( df.loc[df[choice_column] == df[choice_column].min(), ])

    st.subheader('상관관계 분석')
    st.text('컬럼을 2개 이상 선택하면, 컬럼간에 상관계수를 보여드립니다.')
    
    corr_column_list = ['시가', '최고가', '최저가', '종가', '마감가', '거래량']
    selected_columns = st.multiselect('컬럼을 선택하세요.', corr_column_list)
    
    # 2개 이상 선택했을때와 그렇지 않을때로 개발
    if len(selected_columns) >= 2 :
        # 1. 페어플롯을 그린다.
        # todo : 
        # 1) pairplot 을 다른 라이브러리 이용해서 하는 방법
        # 2) pairplot 말고, 반복문으로 두 컬럼씩의 관계를 차트로 그리는 방법
        
        fig1 =  sb.pairplot(data= df, vars=selected_columns)
        st.pyplot(fig1)

        # 2. 상관계수 보여준다.
        st.dataframe(df[selected_columns].corr())
        
    else :
        st.text('컬럼은 2개 이상 선택하여야 합니다.')
