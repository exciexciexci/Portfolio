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
            My Certifications so far:
            - Bachelor's of Science in Marine Engineering
            - Bachelor's of Science in Hotel and Restaurant Management
            - Certified OIC-EW Licensed Marine Engineer Belgium and Philippies
            - x5 NC 2 Tesda Certifications.
            - CSC Professional Level Passer.
            
            If interested in me more you can contact me at my LinkedIn page
            """
            
        )
        st.write("[Linked in page >](https://www.linkedin.com/in/jose-carlo-exciminiano-67597625b/)")
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")