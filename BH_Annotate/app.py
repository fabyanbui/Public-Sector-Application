import streamlit as st
import first_link, second_link, first_tthc, second_tthc

api_key = "AIzaSyDgDvc-ZiRSNqEg9XsZ67Xesm-Gum43PKY"

#AIzaSyBgfCHHuM5aCU6CDOzq8TkmaRUR9CkNNEU
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("👤 Spelling checking trong bộ dữ liệu dịch vụ công")

tab, tab1, tab2, tab3, tab4 = st.tabs(["Home", "First link", "Second link", "First TTHC", "Second TTHC"])

with tab:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_contents = f.read()
    st.markdown(readme_contents, unsafe_allow_html=True)
    
with tab1:
    first_link.main(api=api_key)
with tab2:
    second_link.main(api=api_key)
with tab3:
    first_tthc.main(api=api_key)
with tab4:
    second_tthc.main(api=api_key)

