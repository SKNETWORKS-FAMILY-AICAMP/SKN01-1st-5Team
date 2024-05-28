import streamlit as st
import pandas as pd
import numpy as np
import make_csv
import matplotlib.pyplot as plt
import matplotlib
import platform
from st_on_hover_tabs import on_hover_tabs


from multiapp import MultiApp
from page1 import app as page1
from page2 import app as page2
from home import app as home





# 폰트 파일 경로
font_path = '/Library/Fonts/YourFont.ttf'
font_path = r"C:\Windows\Fonts\malgunbd.ttf"
font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()

plt.rcParams['font.family'] = font_name
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False



# pyplot 관련 에러메시지 제거
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    selected_tab = on_hover_tabs(tabName=['Home', 'About', 'FAQ'], 
                     iconName=['home', 'lightbulb', 'search'],
                     styles = {'navtab': {'background-color':'#000',
                                          'color': '#818181',
                                          'font-size': '15px',
                                          'transition': '.3s',
                                          'white-space': 'nowrap',
                                          'text-transform': 'uppercase'},
                               'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                              'cursor': 'pointer'}},
                               'iconStyle':{'position':'fixed',
                                            'left':'5px',
                                            'text-align': 'left'},
                               'tabStyle' : {'list-style-type': 'none',
                                             'margin-bottom': '15px',
                                             'padding-left': '15px'}},
                     key="1")

# if __name__ == '__main__':
#     app = MultiApp()

#     app.add_app('About', page1)
#     app.add_app('FAQ', page2)
#     app.add_app('Home', home)

#     app.run()
#     import streamlit as st


if selected_tab == 'Home':
    home()
elif selected_tab == 'About':
    page1()
elif selected_tab == 'FAQ':
    page2()
   
  
        
        


