import streamlit as st
import pandas as pd
import time
import human1, human2, recheck

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("👤 Human annotation trong bộ dữ liệu dịch vụ công")

tab, tab1, tab2, tab3= st.tabs(["Home", "First human", "Second human", "Recheck"])

with tab:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_contents = f.read()
    st.markdown(readme_contents, unsafe_allow_html=True)
    
with tab1:
    human1.main()

with tab2:
    human2.main()

with tab3:
    recheck.main()