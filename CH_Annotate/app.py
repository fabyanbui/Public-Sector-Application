import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("👤 Human annotation trong bộ dữ liệu dịch vụ công")

tab, tab1, tab2= st.tabs(["Home", "First human", "Second human"])

with tab:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_contents = f.read()
    st.markdown(readme_contents, unsafe_allow_html=True)
    
with tab1:
    pass

with tab2:
    pass