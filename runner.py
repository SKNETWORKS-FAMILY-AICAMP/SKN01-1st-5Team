import streamlit as st
import pandas as pd
import numpy as np
import source.make_csv as make_csv
import matplotlib.pyplot as plt
import matplotlib
import platform

from source.multiapp import MultiApp
from source.page1 import app as page1
from source.page2 import app as page2

import matplotlib.font_manager as fm

font_path = "C:\\Users\\SAMSUNG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BMJUA_ttf.ttf"
font = fm.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font)

# pyplot 관련 에러메시지 제거
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    app = MultiApp()

    app.add_app('페이지 1', page1)
    app.add_app('페이지 2', page2)

    app.run()