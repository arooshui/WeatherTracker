import streamlit as st

from services.weather_service import get_weather_history

st.title(" Weather History")

history = get_weather_history()

if history:

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No weather history found.")