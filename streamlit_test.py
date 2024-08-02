import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Settings", "About"], menu_icon="cast")

if selected == "Home":
    st.title("Home Page")
    # Your home page content here
elif selected == "Settings":
    st.title("Settings Page")
    # Your settings page content here
elif selected == "About":
    st.title("About Page")
    # Your about page content here
