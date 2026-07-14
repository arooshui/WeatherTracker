import streamlit as st
from services.weather_service import get_weather_history_by_city

st.title(" Search Weather History")
city = st.text_input(
    "Enter City Name",
    placeholder="Example: Hyderabad"
)

if st.button("Search"):

    if city.strip() == "":
        st.warning("Please enter a city.")
    else:
        history = get_weather_history_by_city(city)
        if history:
            st.success(f"Showing weather history for {city}")
            st.dataframe(
                history,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning(f"No weather history found for {city}")