import streamlit as st
from streamlit_lottie import st_lottie
import requests  # Add this import

# Set up the page configuration
st.set_page_config(
    page_title="My Webpage",
    page_icon=":anchor:",
    layout="wide"
)

# Add custom CSS for hover-triggered sidebar animation
st.markdown(
    """
    <style>
    /* Default sidebar state (partially visible) */
    [data-testid="stSidebar"] {
        transform: translateX(-90%); /* Show 10% of the sidebar */
        transition: transform 0.3s ease-out;
        position: relative;
    }

    /* Sidebar state when hovered (fully visible) */
    [data-testid="stSidebar"]:hover {
        transform: translateX(0);
    }

    /* Add a mini bookmark to the left side of the sidebar */
    .sidebar-bookmark {
        position: absolute;
        top: 50%;
        left: 100%; /* Position the bookmark on the left edge of the sidebar */
        transform: translateY(-50%);
        font-size: 14px;
        font-weight: bold;
        color: #ffffff;
        background-color: #4CAF50; /* Green background for the bookmark */
        padding: 5px 10px;
        border-radius: 0 5px 5px 0; /* Rounded corners on the right side */
        writing-mode: vertical-rl; /* Vertical text */
        cursor: pointer;
        z-index: 1; /* Ensure it appears above the sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use a container to organize content
with st.container():
    st.title("Main Page")
    st.sidebar.success("Select a page above")
g
    # Add a mini bookmark to the sidebar
    st.markdown(
        """
        <div class="sidebar-bookmark">More Options</div>
        """,
        unsafe_allow_html=True
    )

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_coding = load_lottieurl("https://lottie.host/94e6d4d4-503b-46f4-b51d-24b3dd67f60b/AfZQAqEfWl.json")

# Main content
with st.container():
    st.subheader("Hi, I'm Exci 👨‍🔧")
    st.title("A Engineer/CSR/Barista from the Philippines")
    st.write("Aspiring Executive Virtual Assistant/Data Analyst.")

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
            - Certified OIC-EW Licensed Marine Engineer Belgium and Philippines
            - x5 NC 2 Tesda Certifications.
            - CSC Professional Level Passer.
            
            If interested in me more, you can contact me at my LinkedIn page.
            """
        )
        st.write("[LinkedIn page >](https://www.linkedin.com/in/jose-carlo-exciminiano-67597625b/)")
        
    with right_column:
        if lottie_coding:  # Check if Lottie animation is loaded
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Failed to load Lottie animation. Please check the URL.")