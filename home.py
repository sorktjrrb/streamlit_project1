import streamlit as st

def run_home():
    st.markdown("### <span style='color: black;'>Microsoft의 주식 가격을 가지고 분석 및 학습하여 향후 주식 가격을 예측하는 앱입니다 :grey_exclamation:</span>", unsafe_allow_html=True)
    st.image('./image/ATFX_Microsoft.jpg', use_column_width=True) 

    st.markdown("<p style='text-align: center; color: black;'><strong>2010-01-04 부터 2024-02-29 까지의 데이터 자료를 가지고 분석하였습니다.</strong></p>", unsafe_allow_html=True)
    # st.write("<center>데이터 출처: <a href='https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset'>https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset</a></center>", unsafe_allow_html=True)
    st.link_button("데이터 출처", "https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset?resource=download",use_container_width=True)
    
    st.markdown("### 기능 소개 :grey_exclamation:")
    st.markdown("이 앱은 Microsoft의 주식 가격 데이터를 사용하여 다음과 같은 기능을 제공합니다:")
    st.markdown("- **주식 데이터 통계 분석 & 시각화**: Microsoft의 주식 가격 데이터를 통계 분석하고 그래프로 표시하여 어떠한 요소들이 주식가격의 영향을 주는지를 한눈에 파악할수 있습니다.")
    st.markdown("- **주식 예측 모델**: 과거 주식 데이터를 사용하여 2가지의 간단한 예측 모델을 구축하고, 시간에 따른 미래 주식 가격과 특정한 날짜의 주식 가격을 예측할 수 있습니다.")