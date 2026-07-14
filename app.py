import streamlit as st

st.set_page_config(
    page_title="Weather API Tracker",
    layout="wide"
)

st.title("Weather API Tracker")

st.markdown("""
## Welcome 

This application allows you to:

-  Fetch current weather for any city
-  Store weather information in MySQL
-  View complete weather history
-  Search weather history by city

Use the **sidebar** to navigate between pages.
""")