import streamlit as st



def main() :
    st.title('MS 주식 가격 예측 앱')

    menu = ['Home','EDA','ML']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        pass
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        pass

if __name__ == '__main__' :
    main()