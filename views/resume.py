import streamlit as st
# from forms.contact import contact_form

st.title("More About Myself")

# Uncomment this function if you want a dialog-based contact form
# @st.dialog("Contact Me")
# def show_contact_form():
#     contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    st.image("Pictures/Profile_pic.jpg", width=180)

with col2:
    st.title("Exciminiano, Jose Carlo", anchor=False)
    st.write(
        "|| OIC-EW Licensed Marine Engineer Kingdom of Belgium/Marina | CSC professional level | Bachelors of Science in Marine Engineering | Bachelors of Science in Hotel and Restaurant Management Graduate ||"
    )
    # Uncomment the following code to add a Contact Me button
    # if st.button("✉️ Contact Me"):
    #     show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Professional Experiences</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - **Customer Support Specialist - TaskUs ; Bulacan Phillipines**, *March 2024 - Present*
    - **OIC-EW Marine Engineer - Exmar PTC ; Makati Philippines | Antwerp Belgium**, *Jan 2019 - Oct 2023*
    - **Barista/Crew Hospitality Taza Mia/The Mills Country Club**, *March 2024 - July  2024*
    """
)

# --- SKILLS ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Professional Licenses</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - **Officer in Charge of Engineering Watch  (Konigreich Belgien)**, *Nov 2024*
    - **Officer in Charge of Engineering Watch (Marina)**, *Feb 2023*
    - **Civil Service Commision Professional Level**, *Aug 2017*
    - **National Certification Level II Tesda**, *May 2014*
    """
)

# --- POSITIONS OF RESPONSIBILITY ---
st.write("\n")
st.markdown(
    """
    <h3 style="text-decoration: underline;">Technical Skills</h3>
    """,
    unsafe_allow_html=True
)
st.write(
    """
    - CRM Proficiency, (Salesforce, THQ.
    - Chat, Web, Email support 
    - Amazon Web Services Phone Inbound and Outbound Phone  Management 
    - MS office / Google suite (Google Apps)` Proficiency  
    - Python
    - and many More
    """
)

# --- RESUME LINK ---
with st.expander("##### **Resume Link**"):
    st.write("Click the link below to view my resume:")
    st.markdown(
        '<a href="https://drive.google.com/file/d/1qazLMAshypavzQrWGM1uq0hJtIW0Pcqq/view?usp=drive_link" target="_blank">**View Resume**</a>',
        unsafe_allow_html=True
    )
