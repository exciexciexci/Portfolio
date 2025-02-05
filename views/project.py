import requests

import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":anchor:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return  r.json()


lottie_coding = load_lottieurl("https://lottie.host/94e6d4d4-503b-46f4-b51d-24b3dd67f60b/AfZQAqEfWl.json")

with st.container():
    st.subheader("Hi, I'm Exci 👨‍🔧")
    st.title("A Engineer/CSR/Barista from the Philipines")
    st.write("Aspiring Excutive Virtual Assistant/Data Analyst.")
  

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            Sorry this page is still under development.
            """
            
        )
        st.write("[Linked in page >](https://www.linkedin.com/in/jose-carlo-exciminiano-67597625b/)")
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")