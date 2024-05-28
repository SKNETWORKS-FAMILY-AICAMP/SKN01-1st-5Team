import streamlit as st
import pandas as pd
import numpy as np


class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, func):
        self.apps.append({
            'title': title,
            'function': func
        })

    def run(self):
        app = st.sidebar.radio(
            'Menu',
            self.apps,
            format_func=lambda app: app['title']
        )

        app['function']()