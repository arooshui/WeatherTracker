import streamlit as st

import pandas as pd
import plotly.express as px

from services.weather_service import (
    get_dashboard_stats,
    get_analytics_data,
    get_all_cities,
    get_weather_condition_distribution,
    get_city_temperature_comparison
)
st.title("Weather Analytics Dashboard")
cities = get_all_cities()

selected_city = st.selectbox(
    "Select City",
    ["All Cities"] + cities
)
st.subheader("Date Filter")

start_date = st.date_input(
    "Start Date"
)

end_date = st.date_input(
    "End Date"
)

stats = get_dashboard_stats(
    selected_city,
    start_date,
    end_date
)

if stats:

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label=" Total Records",
            value=stats["total_records"]
        )

    with col2:
        st.metric(
            label="Unique Cities",
            value=stats["unique_cities"]
        )

    with col3:
        st.metric(
            label=" Avg Temperature",
            value=f"{stats['avg_temperature']} °C"
        )

    with col4:
        st.metric(
            label=" Highest Temp",
            value=f"{stats['max_temperature']} °C"
        )

    with col5:
        st.metric(
            label=" Lowest Temp",
            value=f"{stats['min_temperature']} °C"
        )

else:

    st.error("Unable to load dashboard statistics.")


st.divider()

st.subheader("Weather Trends")

analytics_data = get_analytics_data(
    selected_city,
    start_date,
    end_date
)

if analytics_data:

    df = pd.DataFrame(analytics_data)
    csv = df.to_csv(index=False).encode("utf-8")


    st.download_button(
        label="Download Analytics Data",
        data=csv,
        file_name="weather_analytics.csv",
        mime="text/csv"
    )
    st.subheader(" Temperature Trend")

    temperature_fig = px.line(
        df,
        x="fetched_at",
        y="temperature",
        markers=True,
        title="Temperature Over Time"
    )

    st.plotly_chart(
        temperature_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(" Humidity Trend")

    humidity_fig = px.line(
        df,
        x="fetched_at",
        y="humidity",
        markers=True,
        title="Humidity Over Time"
    )

    st.plotly_chart(
        humidity_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(" Wind Speed Trend")

    wind_fig = px.line(
        df,
        x="fetched_at",
        y="wind_speed",
        markers=True,
        title="Wind Speed Over Time"
    )

    st.plotly_chart(
        wind_fig,
        use_container_width=True
    )

else:

    st.info("No analytics data found for the selected filters.")


st.divider()

st.subheader(" Weather Condition Distribution")

condition_data = get_weather_condition_distribution(
    selected_city,
    start_date,
    end_date
)

if condition_data:

    condition_df = pd.DataFrame(condition_data)

    fig = px.pie(
        condition_df,
        names="weather_condition",
        values="total",
        title="Weather Condition Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("No weather condition data available.")


st.divider()

st.subheader(" Average Temperature by City")

city_data = get_city_temperature_comparison(
    
    start_date,
    end_date
)

if city_data:

    city_df = pd.DataFrame(city_data)

    fig = px.bar(
        city_df,
        x="city",
        y="avg_temperature",
        text="avg_temperature",
        title="Average Temperature by City"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("No city comparison data available.")