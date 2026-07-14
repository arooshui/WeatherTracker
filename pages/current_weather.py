import streamlit as st

from database.db import create_table
from services.weather_service import save_weather

create_table()
st.title(" Current Weather")
city = st.text_input(
    "Enter City",
    placeholder="Example: Hyderabad"
)

if st.button("Fetch Weather"):

    if city.strip() == "":
        st.warning("Please enter a city.")
    else:
        weather = save_weather(city)
        if weather:
            st.success("Weather saved successfully!")
            st.subheader(f"📍 {weather['city']}, {weather['country']}")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    " Temperature",
                    f"{weather['temperature']} °C"
                )

            with col2:
                st.metric(
                    " Humidity",
                    f"{weather['humidity']} %"
                )

            with col3:
                st.metric(
                    " Wind Speed",
                    f"{weather['wind_speed']} km/h"
                )

            with col4:
                st.metric(
                    " Pressure",
                    f"{weather['pressure']} mb"
                )

            st.divider()

            left, right = st.columns(2)

            with left:
                st.write(
                    f"** Condition:** {weather['weather_condition']}"
                )

            with right:
                st.write(
                    f"** Last Updated:** {weather['fetched_at']}"
                )

        else:
            st.error("Unable to fetch weather.")