import streamlit as st
import pandas as pd
from getQuery import get_by_sql

# from crawlingDB.getQuery import get_genesis_by_sql


def app():
    st.image("자동차.jpg", caption=None, use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
   
    if st.button('새로고침'):
        st.experimental_rerun()
    
   
    st.text('점유율이 높은 국내 자동차 브랜드 3사의 FAQ를 모두 제시해주는 통합 FAQ 시스템을 통해\n')
    st.text('검색어를 입력하면 관련 질문에 관련된 답변을 통합적으로 제시합니다.\n3사의 정보를 얻어가세요!')

    keyword = st.text_input("검색어를 입력해주세요 👇")
    
    if keyword:
            st.markdown('### Genesis 답변')
            title, context = get_by_sql('genesis', keyword)
            if len(title) == 0:
                st.write('관련 FAQ가 존재하지 않습니다. 다른 단어로 검색해보세요!')
            else:
                for ti, con in zip(title, context):
                    on = st.toggle(f'**{ti}**')
                    if on:
                        st.write(con)

            st.link_button('**Genesis FAQ 🚗**',url=r'https://www.genesis.com/kr/ko/support/faq.html')

            st.markdown('### KIA 답변')
            title, context = get_by_sql('kia', keyword)            
            if len(title) == 0:
                st.write('관련 FAQ가 존재하지 않습니다. 다른 단어로 검색해보세요!')
            else:
                for ti, con in zip(title, context):
                    on = st.toggle(f'**{ti}**')
                    if on:
                        st.write(con)

            st.link_button('**KIA FAQ 🚗**',url=r'https://www.kia.com/kr/customer-service/center/faq')
            


            
        



    
    
        

