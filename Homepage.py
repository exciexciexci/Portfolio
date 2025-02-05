import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon="🎉",  # Use a valid emoji or icon
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

    # Add a mini bookmark to the sidebar
    st.markdown(
        """
        <div class="sidebar-bookmark">More Options</div>
        """,
        unsafe_allow_html=True
    )
    
