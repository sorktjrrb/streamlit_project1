# **streamlit_project1 (MicroSoft 주식 가격 예측 프로젝트)**

------
## 👨‍🏫 프로젝트 소개

> 이 프로젝트는 최근 AI 기술에 대한 관심이 높아지면서 AI와 관련된 기업들의 주식 시장이 큰 관심을 받고 있는 상황에서 시작되었습니다.

> 특히, 앤비디아(NVIDIA)와 마이크로소프트(Microsoft)와 같은 기업은 AI 기술에 대한 지속적인 투자와 연구 개발을 통해 선도적인 역할을 하고 있습니다. 더불어, 최근에는 애플(Apple)도 AI 개발에 대한 목표를 선언하면서 주식 시장에서의 AI 기업들에 대한 관심이 더욱 높아지고 있습니다.

> 이러한 AI 기술과 관련된 기업들의 동향과 주식 시장의 변화를 파악하고자, 이 프로젝트는 주식 시장에서의 AI 기업들의 주가를 예측하는 머신러닝 모델을 개발하는 것을 목표로 하고 있습니다.

> 이중에서도 **"MicroSoft의 향후 주식 동향 파악"** 을 주제로 한 앱입니다.

------
## 📌 주요 기능

- 주식 데이터 분석 및 가공
- 주식 데이터 시각화
- 시계열 데이터 분석
- 머신러닝을 활용한 주식 가격 예측
- Streamlit을 사용한 앱 대시보드 구축

------
## 🖱 배포 주소
> URL : <http://ec2-13-209-11-253.ap-northeast-2.compute.amazonaws.com:8501>

------
## 💻 개발 환경 및 기술 스택
jupyter notebook을 통해, msft_stock_data.csv 파일을 통계 분석하고, Prophet을 통해 주식가격에대한 시계열 예측 분석을 진행 하였습니다.

Prophet 분석 데이터를 통해 시간에 따른 주식 가격 변동에 유의미한점을 확인하였고, 이 데이터까지 포함하여 선형 회귀 (Linear regression) 모델을 개발하고  MicroSoft의 주식 가격을 예측하는 머신러닝을 수행하였습니다.

최종적으로 Streamlit을 이용해서, 통계 분석과 데이터 시각화 및 주식 가격을 예측하는 대시보드 앱을 개발하였고, AWS EC2를 사용하여 서버에 배포하였습니다.

- **데이터 분석 및 시각화**

<img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=black"><img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"><img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"><img src="https://img.shields.io/badge/matplotlib-013243?style=for-the-badge&logo=matplotlib&logoColor=white"></br>
- **시계열 데이터 분석**

<img src="https://img.shields.io/badge/Prophet-E6522C?style=for-the-badge&logo=prometheus&logoColor=white"></br>
- **머신러닝 모델링**

<img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"></br>
- **웹 애플리케이션 개발**

<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"></br>
- **버전 관리**

<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"></br>
- **편집기**

<img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white"></br>
- **서버**

<img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"></br>

------
## 🧨 트러블 슈팅
#### 1) 앱화면에 시인성을 높이기 위해 이모티콘을 넣어 수정하던 중 이모티콘을 인식하지 못하고 문구가 깨지는 이슈 발생
- 원인 : 가운데 정렬 및 문구 색체를 다르게 하기위해 마크다운과 html 구문을 활용하여 작성하였던 구문이 이모티콘 구문을 인식하지 못하여 발생 (:chart:)
```
st.markdown('<h1 style="text-align: center; color: black; display: flex; align-items: center;"><img src="https://img.hankyung.com/photo/202111/01.27950322.1.jpg" alt="plane" style="max-width: 2em; max-height: 2em; margin-right: 0.5em;">Microsoft 주가 예측 앱 :chart:;</h1>', unsafe_allow_html=True)
```
- 해결 : 검색을 통하여 HTML 또는 XML에서 사용되는 문자 참조(entity reference)로 수정하여야 한다는걸 확인하였고, ChatGPT를 활용하여 문구를 수정하여 정상 출력되는것을 확인하였습니다. (&#x1F4B9)
```
st.markdown('<h1 style="text-align: center; color: black; display: flex; align-items: center;"><img src="https://img.hankyung.com/photo/202111/01.27950322.1.jpg" alt="plane" style="max-width: 2em; max-height: 2em; margin-right: 0.5em;">Microsoft 주가 예측 앱 &#x1F4B9;</h1>', unsafe_allow_html=True)
```


#### 2) 기존 streamlit.sidebar.selectbox 로 메뉴를 구성하였을경우 화면 전환시 메뉴창이 버벅거리는 부분이 생겨 시인성도 높이기위해 사이드바 커스텀을 진행하던중 메뉴 자체가 사라져버리는 이슈 발생
- 원인 : 사이드바 커스텀을 적용하기 위해선 stremalit-option-menu 라이브러리를 추가적으로 설치하여 수정하여야 정상적으로 화면에 출력되는데, 설치없이 수정한 부분을 인식하지 못하여 발생
- 해결 : 검색을 통하여 새로운 라이브러리 설치 및 수정을 통해서 정상적으로 출력 확인
- 수정 내용 및 이미지 블로그로 작성 : <https://sorktjrrb.tistory.com/96>

#### 3) 사용자가 선택한 날짜데이터를 time값으로 변환시켜주기위해서 넣은 구문이 호환되지 않아 계속 데이터가 없는것으로 인식하는 이슈 발생
- 원인 : streamlit.data_input 으로 들어오는 데이터 타입 확인결과 'datetime.date' 로 들어오는걸 확인. 데이터프레임의 데이터 타입 'datetime64[ns]' 와 타입이 같지않아 없는데이터로 인식하여 문제 발생
```
selected_date = st.date_input('날짜를 선택하세요', value=pd.to_datetime('2024-12-31'))
    print(type(selected_date))

<class 'datetime.date'>
```
- 해결 : 기존 데이터프레임의 'Date' 컬럼값을 apply 함수를 이용하여 datetime.date 타입으로 변경하여 적용하여 정상 출력되는것 확인
```
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
    print(type(selected_date))
```
------
## ✏ 작성자
- 강석규
- e-mail : sorktjrrb@naver.com
------
