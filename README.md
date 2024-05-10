# **MicroSoft 주식 가격 예측 프로젝트**

------
## 👨‍🏫 프로젝트 소개

이 프로젝트는 최근 AI 기술에 대한 관심이 높아지면서 AI와 관련된 기업들의 주식 시장이 큰 관심을 받고 있는 상황에서 시작되었습니다.

특히, 앤비디아(NVIDIA)와 마이크로소프트(Microsoft)와 같은 기업은 AI 기술에 대한 지속적인 투자와 연구 개발을 통해 선도적인 역할을 하고 있습니다. 더불어, 최근에는 애플(Apple)도 AI 개발에 대한 목표를 선언하면서 주식 시장에서의 AI 기업들에 대한 관심이 더욱 높아지고 있습니다.

이러한 AI 기술과 관련된 기업들의 동향과 주식 시장의 변화를 파악하고자, 이 프로젝트는 주식 시장에서의 AI 기업들의 주가를 예측하는 머신러닝 모델을 개발하는 것을 목표로 하고 있습니다.

이중에서도 **"Microsoft의 향후 주식 동향 파악"** 을 주제로 한 앱입니다.

------
## 📌 주요 기능

- 주식 데이터 분석 및 가공
- 주식 데이터 시각화
- 시계열 데이터 분석
- 머신러닝을 활용한 주식 가격 예측
- Streamlit을 사용한 앱 대시보드 구축

------
## 💻 개발 환경 및 기술 스택
- **데이터 분석과 가공 및 시각화**
<br><img src="https://img.shields.io/badge/anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white">&nbsp;<img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=black">&nbsp;<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">&nbsp;<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">&nbsp;<img src="https://img.shields.io/badge/matplotlib-50C878?style=for-the-badge&logo=matplotlib&logoColor=white">&nbsp;<img src="https://img.shields.io/badge/seaborn-50C878?style=for-the-badge&logo=seaborn&logoColor=white">&nbsp;<img src="https://img.shields.io/badge/joblib-7C3AED?style=for-the-badge&logo=joblib&logoColor=white"></br>

- **시계열 데이터 분석**
<br><img src="https://img.shields.io/badge/Prophet-E6522C?style=for-the-badge&logo=prometheus&logoColor=white">

- **머신러닝 모델링 및 관리**
<br><img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"></br>

- **앱 대시보드 개발**
<br><img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"></br>

- **버전 관리**
<br><img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"></br>

- **편집기**
<br><img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white"></br>

- **서버**
<br><img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"></br>

------
## 🖱 개발 과정
 - **데이터 분석과 가공 및 시각화**

> 데이터셋 : <https://www.kaggle.com/datasets/muhammadibrahimqasmi/microsft-dataset?resource=download>
1) jupyter notebook 개발 환경에서, pandas 라이브러리를 활용하여 데이터셋 파일을 읽어와 통계 분석 및 상관 관계 분석을 진행 하였습니다.
2) 분석한 데이터를 가지고 Prophet을 진행하였고, 시간에 따른 주식 가격 변동이 유의미하게 적용된다는걸 matplotlib와 seaborn 라이브러리를 통해 시각화하여 명확하게 확인해볼수 있었습니다.
3) 유의미한게 확인된 날짜 데이터를 'time'라는 컬럼값으로 추가하여 데이터를 가공하였고, 사용자가 직접 계산하지 않고 자동으로 불러올수 있도록 numpy 라이브러리를 사용하여 날짜데이터와 time값을 1년뒤에것까지 새로운 데이터로 생성하였습니다.

- **머신러닝 모델링 및 관리**
1) sklearn 라이브러리의 Linear regression 모델을 개발하고 MicroSoft의 주식 가격을 예측하는 머신러닝을 수행하였습니다.
2) 완성된 모델은 joblib 라이브러리를 통해 저장하였습니다.

- **앱 대시보드 개발**
1) GitHub 에 새로운 repository를 생성하여 Visual Studio Code 통합 개발 환경과 연동해 파일별로 구분하고, 가공된 데이터과 모델을 읽어와 Stremalit 라이브러리를 통해 통계 분석과 데이터 시각화 및 주식 가격을 예측하는 앱 대시보드를 개발하였습니다.
2) GitHub Desktop을 통해 버전 관리(commit, pull, clone)를 하였고, 중간작업은 vscode를 통해 수정 작업과 보완할점을 개선하였습니다.

- **서버 배포 및 자동화**
1) ASW의 EC2 인스턴스를 Linux OS로 생성하였습니다. Putty 프로토콜을 통해 EC2 Linux 서버에 접속하여 Anaconda 프롬포트 설치 및 가상환경을 생성하여 서버에 배포하였습니다.
2) GitHub 의 Actions를 생성하여 추후에 수정사항들이 반영될수있도록 최종 자동화까지 진행하였습니다.

------
## 📄 배포 주소
> URL : <http://ec2-13-209-11-253.ap-northeast-2.compute.amazonaws.com:8501>

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
- 정상 동작을 위해 설치 필요
```
from streamlit_option_menu import option_menu
```
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
