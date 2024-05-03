import streamlit as st

def run_home():
    st.markdown("<h2 style='text-align: center; color: black;'>Microsoft의 주식 가격을 가지고 분석 및 학습하여 향후 주식 가격을 예측하는 앱입니다</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'>2010-01-04 부터 2024-02-29 까지의 데이터를 가지고 분석하였습니다.</p>", unsafe_allow_html=True)
    st.link_button("데이터 출처", "https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset?resource=download",use_container_width=True)

    st.image('./image/ATFX_Microsoft.jpg', use_column_width=True)

    