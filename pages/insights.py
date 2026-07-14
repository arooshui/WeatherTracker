import streamlit as st
import pandas as pd
import plotly.express as px
from services.weather_service import (
    get_all_cities,
    get_analytics_data,
    predict_weather_by_city
)

from utils.logger import logger


st.set_page_config(
    page_title="Weather Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Weather Insights Dashboard")

logger.info("Weather Insights page loaded.")

cities = get_all_cities()

selected_city = st.selectbox(
    "Select City",
    ["All Cities"] + cities
)

start_date = st.date_input(
    "Start Date"
)

end_date = st.date_input(
    "End Date"
)

try:

    logger.info("Fetching analytics data.")

    analytics_data = get_analytics_data(
        selected_city,
        start_date,
        end_date
    )

    if not analytics_data:

        st.warning("No data available.")

        st.stop()

    df = pd.DataFrame(analytics_data)

    st.success(f"{len(df)} records loaded successfully.")

except Exception:

    logger.exception("Failed to load analytics data.")

    st.error("Unable to load analytics data.")


import plotly.graph_objects as go

st.divider()

st.subheader("🌡️ Temperature vs 💧 Humidity Analysis")

try:

    logger.info("Generating Temperature vs Humidity graph.")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["fetched_at"],
            y=df["temperature"],
            mode="lines+markers",
            name="Temperature (°C)"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["fetched_at"],
            y=df["humidity"],
            mode="lines+markers",
            name="Humidity (%)",
            yaxis="y2"
        )
    )

    fig.update_layout(
        title="Temperature vs Humidity",
        xaxis_title="Date & Time",

        yaxis=dict(
            title="Temperature (°C)"
        ),

        yaxis2=dict(
            title="Humidity (%)",
            overlaying="y",
            side="right"
        ),

        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except Exception:

    logger.exception("Failed to generate Temperature vs Humidity graph.")

    st.error("Unable to generate graph.")


st.divider()

st.subheader("📊 Weather Observations")

try:

    logger.info("Generating weather observations.")

    avg_temp = df["temperature"].mean()
    avg_humidity = df["humidity"].mean()

    max_temp = df["temperature"].max()
    min_temp = df["temperature"].min()

    max_humidity = df["humidity"].max()
    min_humidity = df["humidity"].min()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🌡️ Average Temperature",
            f"{avg_temp:.2f} °C"
        )

        st.metric(
            "🔥 Highest Temperature",
            f"{max_temp:.2f} °C"
        )

        st.metric(
            "❄️ Lowest Temperature",
            f"{min_temp:.2f} °C"
        )

    with col2:

        st.metric(
            "💧 Average Humidity",
            f"{avg_humidity:.2f} %"
        )

        st.metric(
            "💦 Highest Humidity",
            f"{max_humidity:.2f} %"
        )

        st.metric(
            "🏜️ Lowest Humidity",
            f"{min_humidity:.2f} %"
        )

except Exception:

    logger.exception("Failed to generate weather observations.")

    st.error("Unable to generate observations.")

st.divider()

st.subheader("📈 Correlation Analysis")

try:

    logger.info("Calculating temperature and humidity correlation.")

    correlation = df["temperature"].corr(df["humidity"])

    st.metric(
        "Correlation Coefficient",
        f"{correlation:.2f}"
    )

    if correlation >= 0.7:

        st.success(
            "Strong Positive Correlation\n\n"
            "Temperature and humidity tend to increase together."
        )

    elif correlation >= 0.3:

        st.info(
            "Moderate Positive Correlation\n\n"
            "Temperature and humidity have a slight positive relationship."
        )

    elif correlation > -0.3:

        st.warning(
            "Weak Correlation\n\n"
            "Temperature and humidity do not show a strong relationship."
        )

    elif correlation > -0.7:

        st.info(
            "Moderate Negative Correlation\n\n"
            "As temperature increases, humidity tends to decrease."
        )

    else:

        st.success(
            "Strong Negative Correlation\n\n"
            "Higher temperatures are generally associated with lower humidity."
        )

except Exception:

    logger.exception("Failed to calculate correlation.")

    st.error("Unable to calculate correlation.")

st.divider()

st.subheader("🔵 Temperature vs Humidity Scatter Plot")

try:

    logger.info("Generating Temperature vs Humidity Scatter Plot.")

    scatter_fig = px.scatter(
        df,
        x="temperature",
        y="humidity",
        color="weather_condition",
        size="wind_speed",
        hover_data=[
            "city",
            "pressure",
            "fetched_at"
        ],
        title="Relationship Between Temperature and Humidity"
    )

    scatter_fig.update_layout(
        xaxis_title="Temperature (°C)",
        yaxis_title="Humidity (%)"
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

except Exception:

    logger.exception("Failed to generate scatter plot.")

    st.error("Unable to generate scatter plot.")


st.divider()

st.subheader("🔥 Correlation Heatmap")

try:

    logger.info("Generating correlation heatmap.")

    numeric_df = df[
        [
            "temperature",
            "humidity",
            "pressure",
            "wind_speed"
        ]
    ]

    correlation_matrix = numeric_df.corr()

    heatmap = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Between Weather Variables"
    )

    st.plotly_chart(
        heatmap,
        use_container_width=True
    )

except Exception:

    logger.exception("Failed to generate correlation heatmap.")

    st.error("Unable to generate correlation heatmap.")

st.divider()

st.subheader("🌤 Weather Condition Analysis")

try:

    logger.info("Generating weather condition analysis.")

    condition_summary = (
        df.groupby("weather_condition")
        .agg(
            average_temperature=("temperature", "mean"),
            average_humidity=("humidity", "mean"),
            average_pressure=("pressure", "mean"),
            average_wind_speed=("wind_speed", "mean"),
            total_records=("weather_condition", "count")
        )
        .reset_index()
    )

    st.dataframe(
        condition_summary,
        use_container_width=True
    )

    st.subheader("📋 Insights")

    for _, row in condition_summary.iterrows():

        st.markdown(f"### {row['weather_condition']}")

        st.write(
            f"• Observed **{int(row['total_records'])}** times in the selected period."
        )

        st.write(
            f"• Average Temperature : **{row['average_temperature']:.2f} °C**"
        )

        st.write(
            f"• Average Humidity : **{row['average_humidity']:.2f} %**"
        )

        st.write(
            f"• Average Pressure : **{row['average_pressure']:.2f} mb**"
        )

        st.write(
            f"• Average Wind Speed : **{row['average_wind_speed']:.2f} km/h**"
        )

        if row["average_humidity"] >= 80:

            st.success(
                "This weather condition is generally associated with HIGH humidity."
            )

        elif row["average_humidity"] >= 60:

            st.info(
                "This weather condition is generally associated with MODERATE humidity."
            )

        else:

            st.warning(
                "This weather condition is generally associated with LOW humidity."
            )

        if row["average_temperature"] >= 35:

            st.write(
                "🔥 Usually occurs during high temperatures."
            )

        elif row["average_temperature"] >= 25:

            st.write(
                "🌤 Usually occurs during moderate temperatures."
            )

        else:

            st.write(
                "❄️ Usually occurs during lower temperatures."
            )

        if row["average_pressure"] < 1005:

            st.write(
                "📉 Lower atmospheric pressure is commonly observed."
            )

        else:

            st.write(
                "📈 Higher atmospheric pressure is commonly observed."
            )

        st.divider()

except Exception:

    logger.exception("Failed to generate weather condition analysis.")

    st.error("Unable to generate weather condition analysis.")

st.divider()

st.subheader("🔮 Weather Prediction")

try:

    logger.info("Generating weather prediction.")

    latest = df.iloc[-1]

    prediction = "Unknown"

    reasons = []

    if latest["humidity"] >= 80:

        prediction = "🌧️ Rainy"

        reasons.append("High humidity detected.")

    if latest["pressure"] <= 1005:

        reasons.append("Atmospheric pressure is low.")

    if latest["temperature"] >= 35:

        prediction = "☀️ Sunny"

        reasons.append("Temperature is very high.")

    elif 25 <= latest["temperature"] < 35:

        prediction = "⛅ Cloudy"

        reasons.append("Temperature is moderate.")

    if latest["wind_speed"] >= 20:

        reasons.append("Wind speed is relatively high.")

    st.success(f"Predicted Weather : {prediction}")

    st.subheader("Reason")

    for reason in reasons:

        st.write(f"• {reason}")

except Exception:

    logger.exception("Failed to generate weather prediction.")

    st.error("Unable to generate prediction.")


st.divider()

st.subheader("🔮 Predict Weather")

prediction_city = st.selectbox(
    "Select City for Prediction",
    get_all_cities()
)

if st.button("Predict"):

    prediction = predict_weather_by_city(prediction_city)

    if prediction is None:

        st.error("No historical data available.")

    else:

        latest = prediction["latest"]

        result = prediction["prediction"]

        st.success(
            f"Predicted Weather Condition : {result['weather_condition']}"
        )

        st.subheader("Current Weather Record")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Temperature",
                f"{latest['temperature']} °C"
            )

            st.metric(
                "Humidity",
                f"{latest['humidity']} %"
            )

        with col2:

            st.metric(
                "Pressure",
                f"{latest['pressure']} mb"
            )

            st.metric(
                "Wind Speed",
                f"{latest['wind_speed']} km/h"
            )

        st.divider()

        st.subheader("Closest Historical Average")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Temperature",
                f"{result['average_temperature']:.2f} °C"
            )

            st.metric(
                "Humidity",
                f"{result['average_humidity']:.2f} %"
            )

        with col2:

            st.metric(
                "Pressure",
                f"{result['average_pressure']:.2f} mb"
            )

            st.metric(
                "Wind Speed",
                f"{result['average_wind_speed']:.2f} km/h"
            )

        st.divider()

        st.info(
            "Prediction is based on the closest historical weather pattern for the selected city."
        )
    
st.divider()

st.subheader("📈 Trend Detection")

try:

    logger.info("Generating trend detection.")

    midpoint = len(df) // 2

    first_half = df.iloc[:midpoint]

    second_half = df.iloc[midpoint:]

    first_temp = first_half["temperature"].mean()
    second_temp = second_half["temperature"].mean()

    first_humidity = first_half["humidity"].mean()
    second_humidity = second_half["humidity"].mean()

    first_pressure = first_half["pressure"].mean()
    second_pressure = second_half["pressure"].mean()

    first_wind = first_half["wind_speed"].mean()
    second_wind = second_half["wind_speed"].mean()

    st.subheader("🌡 Temperature Trend")

    if second_temp > first_temp:

        st.success(
            f"Average temperature increased from {first_temp:.2f}°C to {second_temp:.2f}°C."
        )

    elif second_temp < first_temp:

        st.warning(
            f"Average temperature decreased from {first_temp:.2f}°C to {second_temp:.2f}°C."
        )

    else:

        st.info("Average temperature remained stable.")

    st.subheader("💧 Humidity Trend")

    if second_humidity > first_humidity:

        st.success(
            f"Average humidity increased from {first_humidity:.2f}% to {second_humidity:.2f}%."
        )

    elif second_humidity < first_humidity:

        st.warning(
            f"Average humidity decreased from {first_humidity:.2f}% to {second_humidity:.2f}%."
        )

    else:

        st.info("Average humidity remained stable.")

    st.subheader("📊 Pressure Trend")

    if second_pressure > first_pressure:

        st.success(
            f"Average pressure increased from {first_pressure:.2f} mb to {second_pressure:.2f} mb."
        )

    elif second_pressure < first_pressure:

        st.warning(
            f"Average pressure decreased from {first_pressure:.2f} mb to {second_pressure:.2f} mb."
        )

    else:

        st.info("Average pressure remained stable.")

    st.subheader("🌬 Wind Speed Trend")

    if second_wind > first_wind:

        st.success(
            f"Average wind speed increased from {first_wind:.2f} km/h to {second_wind:.2f} km/h."
        )

    elif second_wind < first_wind:

        st.warning(
            f"Average wind speed decreased from {first_wind:.2f} km/h to {second_wind:.2f} km/h."
        )

    else:

        st.info("Average wind speed remained stable.")

    st.subheader("☁ Most Frequent Weather")

    most_common = df["weather_condition"].mode()[0]

    st.info(
        f"The most frequently observed weather condition is **{most_common}**."
    )

except Exception:

    logger.exception("Failed to generate trend detection.")

    st.error("Unable to generate trend detection.")


st.divider()

def detect_outliers(df, column):

    q1 = df[column].quantile(0.25)

    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - (1.5 * iqr)

    upper_limit = q3 + (1.5 * iqr)

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "outliers": outliers
    }

st.divider()

st.subheader("🚨 Outlier Detection using IQR")

try:

    logger.info("Detecting outliers.")

    metrics = [
        "temperature",
        "humidity",
        "pressure",
        "wind_speed"
    ]

    for metric in metrics:

        st.subheader(metric.replace("_", " ").title())

        result = detect_outliers(
            df,
            metric
        )

        st.write(f"Q1 : {result['q1']:.2f}")

        st.write(f"Q3 : {result['q3']:.2f}")

        st.write(f"IQR : {result['iqr']:.2f}")

        st.write(f"Lower Limit : {result['lower_limit']:.2f}")

        st.write(f"Upper Limit : {result['upper_limit']:.2f}")

        if result["outliers"].empty:

            st.success(
                f"No {metric} outliers detected."
            )

        else:

            st.error(
                f"{len(result['outliers'])} outlier(s) detected."
            )

            st.dataframe(
                result["outliers"][
                    [
                        "city",
                        metric,
                        "weather_condition",
                        "fetched_at"
                    ]
                ],
                use_container_width=True
            )

        st.divider()

except Exception:

    logger.exception("Failed to detect outliers.")

    st.error("Unable to detect outliers.")