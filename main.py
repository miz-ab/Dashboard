import aboutUs
import EDA
import streamlit as st

PAGES = {
    "Exploring the Data" : EDA,
    "About Us": aboutUs
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()