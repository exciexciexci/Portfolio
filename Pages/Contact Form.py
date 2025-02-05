import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the page
st.set_page_config(page_title="Contact Form", page_icon="📧")

# Custom CSS for styling
st.markdown("""
    <style>
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title("Contact Me 📨")
st.write("Fill out the form below to get in touch!")

# Contact form
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Your name")
    email = st.text_input("Email", placeholder="Your email address")
    message = st.text_area("Message", placeholder="Your message here...")
    submit_button = st.form_submit_button("Submit")

    # If the form is submitted
    if submit_button:
        if name and email and message:
            # Email configuration
            sender_email = "your_email@gmail.com"  # Replace with your email
            receiver_email = "your_email@gmail.com"  # Replace with your email
            password = "your_email_password"  # Replace with your email password

            # Create the email
            subject = f"New Contact Form Submission from {name}"
            body = f"""
            Name: {name}
            Email: {email}
            Message: {message}
            """

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                st.success("Your message has been sent successfully! 🎉")
            except Exception as e:
                st.error(f"An error occurred while sending the email: {e}")
        else:
            st.warning("Please fill out all fields before submitting.")