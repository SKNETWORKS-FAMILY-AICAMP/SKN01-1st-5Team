import streamlit as st
import pandas as pd
import numpy as np
from source import make_csv
import matplotlib.pyplot as plt
import matplotlib
import platform
import seaborn as sns
matplotlib.use("Agg")

import matplotlib.font_manager as fm

# 폰트 파일 경로
font_path = '/Library/Fonts/YourFont.ttf'
font_path = r"C:\Windows\Fonts\malgunbd.ttf"
font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()

plt.rcParams['font.family'] = font_name
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False


# pyplot 관련 에러메시지 제거
st.set_option('deprecation.showPyplotGlobalUse', False)


@st.cache_data
def load_data():
    data1, data2, data3 = make_csv.make_dataframe()
    return data1, data2, data3
   


def app():
    df1, df2, df3 = load_data()
    st.markdown("<h1 style='text-align: center;'>ABOUT</h1>", unsafe_allow_html=True)

    # 차량등록현황
    # st.markdown("<h2 style='text-align: center; color: black;'>연도별 차량등록현황</h2>", unsafe_allow_html=True)
    multi = '''
    
           
            매년 차량 수요가 증가함에 대응하여 
            차량 구매, 차량 정비 등 차에 대한 정보가 필요한
            소비자들의 다양한 궁금증을 해결을 위해
            국내 자동차 시장 점유율 :blue[TOP3 기업의 FAQ]를 통합하여 제시해주고자 합니다.
            이로써 사용자들이 다양한 브랜드의 정보를 비교하고,
            보다 현명한 구매 결정을 내릴 수 있도록 돕는 것을 목표로 합니다.
            
            
            
            아래는 차량 수요가 증가하고 있음을 보여주는 지표입니다.
  
    '''
    st.markdown(multi)
    
    
    
    multi = '''
            :sparkles: 전국 자동차 등록 현황 :sparkles:
        
            차량 등록 현황의 증가는 국내 시장에서 차량 수요가 증가하고 있음을 나타냅니다.
    '''
        
    st.markdown(multi)
    
    region = st.selectbox("", df3['시도명(1)'].unique())
    region_data = df3[df3['시도명(1)'] == region].drop(columns=['시도명(1)', '시군구(1)']).transpose()
    region_data.columns = [region]
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.plot(region_data, label=region)
    ax.set_title(f'{region} 연도별 차량 등록 변화', fontsize = 20)
    ax.set_xlabel('연도',  fontsize = 15)
    ax.set_ylabel('차량 등록 수',  fontsize = 15)
    ax.legend()
    st.pyplot(fig)

    # 차량 수출액 변화
    # st.markdown("<h2 style='text-align: center; color: black;'>연도별 수출액 변화</h2>", unsafe_allow_html=True)
    multi = '''
            :sparkles: 자동차 수출액 :sparkles:
            
            차량 수출액의 증가는 국제 시장에서 차량 수요가 증가하고 있음을 나타냅니다.
            차량 수출액이 증가한다는 것은 국내 생산된 차량이 해외 시장에서 
            더 많이 판매되고 있음을 의미합니다.
            
    '''
    st.markdown(multi)
    
    fig, ax1 = plt.subplots()
    ax1.plot(df1['연도'], df1['차량등록현황'], color='red', marker='o')
    ax1.set_xlabel('연도')  # x축 이름 설정
    ax1.set_ylabel('차량등록현황', color='red')  # 첫 번째 y축 이름 설정
    ax1.tick_params(axis='y', labelcolor='red')    
    # 두 번째 y축 (수출액)
    ax2 = ax1.twinx()
    ax2.plot(df1['연도'], df2['수출액'], color='blue', marker='o')
    ax2.set_ylabel('수출액', color='blue')  # 두 번째 y축 이름 설정
    ax2.tick_params(axis='y', labelcolor='blue')    
    # Streamlit에 플롯 표시
    st.pyplot(fig)
        
        
    
    

   

