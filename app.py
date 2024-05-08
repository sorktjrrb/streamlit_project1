from PIL import Image
from home import run_home
from eda import run_eda
from graph import run_graph
from ml import run_ml

import streamlit as st
from streamlit_option_menu import option_menu


def main():
    #st.markdown('<h1 style="text-align: center; color: black; display: flex; align-items: center;"><img src="https://img.hankyung.com/photo/202111/01.27950322.1.jpg" alt="plane" style="max-width: 1em; margin-right: 0.5em;"> Microsoft 주가 예측 앱 &#x1F4B9;</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; color: black; display: flex; align-items: center;"><img src="https://img.hankyung.com/photo/202111/01.27950322.1.jpg" alt="plane" style="max-width: 2em; max-height: 2em; margin-right: 0.5em;">Microsoft 주가 예측 앱 &#x1F4B9;</h1>', unsafe_allow_html=True)

    menu = ['메인 화면','데이터 통계 분석','시간에 따른 가격 예측','특정 날짜의 가격 예측']

    # choice = st.sidebar.selectbox('메뉴', menu)

    with st.sidebar:
        choice = option_menu("Menu", menu,
                         icons=['house', 'kanban', 'bi bi-robot', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#38B3E3"},
        }
        )
    
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_graph()
    elif choice == menu[3] :
        run_ml()

if __name__ == '__main__' :
    main()

# Date 날짜: 주식 데이터의 날짜입니다.
# Open 시가: 해당 날짜의 주식 시가입니다.
# High 최고가: 해당 날짜의 주식 최고 가격입니다.
# Low 최저가: 해당 날짜의 주식 최저 가격입니다.
# Close 마감: 해당 날짜의 주식 마감 가격입니다.
# Adj Close	 조정 마감: 배당금 및 주식 분할과 같은 기업 활동을 고려한 해당 날짜의 조정된 주식 마감 가격입니다. (종가)
# 거래량: 해당 날짜의 주식 거래량, 즉 거래된 주식 수입니다.

# 데이터 출처 : https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset?resource=download