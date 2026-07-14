from database.db import get_connection, create_table
from services.weather_api import get_weather
from utils.logger import logger


def save_weather(city):

    weather = get_weather(city)

    if weather is None:
        logger.warning(f"Weather data not found for city: {city}")
        return None

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO weather_data(city, country, latitude, longitude,
    temperature, humidity, pressure, wind_speed,
    weather_condition, fetched_at)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        weather["city"],
        weather["country"],
        weather["latitude"],
        weather["longitude"],
        weather["temperature"],
        weather["humidity"],
        weather["pressure"],
        weather["wind_speed"],
        weather["weather_condition"],
        weather["fetched_at"]
    )

    try:

        cursor.execute(insert_query, values)

        connection.commit()

        logger.info(f"Weather data saved successfully for city: {city}")

        return weather

    except Exception as e:

        logger.exception(f"Failed to save weather data for city: {city}")

        return None

    finally:

        cursor.close()
        connection.close()


def get_weather_history():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        city,
        country,
        temperature,
        humidity,
        pressure,
        wind_speed,
        weather_condition,
        fetched_at
    FROM weather_data
    ORDER BY fetched_at DESC
    """

    try:

        logger.info("Fetching complete weather history.")

        cursor.execute(query)

        history = cursor.fetchall()

        return history

    except Exception as e:

        logger.exception("Failed to fetch weather history.")

        return []

    finally:

        cursor.close()
        connection.close()


def get_weather_history_by_city(city):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        city,
        country,
        temperature,
        humidity,
        pressure,
        wind_speed,
        weather_condition,
        fetched_at
    FROM weather_data
    WHERE city = %s
    ORDER BY fetched_at DESC
    """

    try:

        logger.info(f"Fetching weather history for city: {city}")

        cursor.execute(query, (city,))

        history = cursor.fetchall()

        return history

    except Exception as e:

        logger.exception(f"Failed to fetch weather history for city: {city}")

        return []

    finally:

        cursor.close()
        connection.close()

def get_dashboard_stats(city=None, start_date=None, end_date=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        COUNT(*) AS total_records,
        COUNT(DISTINCT city) AS unique_cities,
        ROUND(AVG(temperature),2) AS avg_temperature,
        MAX(temperature) AS max_temperature,
        MIN(temperature) AS min_temperature
    FROM weather_data
    WHERE 1=1
    """

    values = []

    if city and city != "All Cities":
        query += " AND city = %s"
        values.append(city)

    if start_date and end_date:
        query += " AND DATE(fetched_at) BETWEEN %s AND %s"
        values.extend([start_date, end_date])

    try:

        logger.info(
            f"Fetching dashboard statistics | City: {city}, Start: {start_date}, End: {end_date}"
        )

        cursor.execute(query, tuple(values))

        return cursor.fetchone()

    except Exception as e:

        logger.exception("Failed to fetch dashboard statistics.")

        return None

    finally:

        cursor.close()
        connection.close()


def get_analytics_data(city=None, start_date=None, end_date=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        city,
        temperature,
        humidity,
        wind_speed,
        pressure,
        weather_condition,
        fetched_at
    FROM weather_data
    WHERE 1=1
    """

    values = []

    if city and city != "All Cities":
        query += " AND city = %s"
        values.append(city)

    if start_date and end_date:
        query += " AND DATE(fetched_at) BETWEEN %s AND %s"
        values.extend([start_date, end_date])

    query += " ORDER BY fetched_at"

    try:

        logger.info(
            f"Fetching analytics data | City: {city}, Start: {start_date}, End: {end_date}"
        )

        cursor.execute(query, tuple(values))

        return cursor.fetchall()

    except Exception as e:

        logger.exception("Failed to fetch analytics data.")

        return []

    finally:

        cursor.close()
        connection.close()


def get_all_cities():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT DISTINCT city
    FROM weather_data
    ORDER BY city
    """

    try:

        logger.info("Fetching available cities.")

        cursor.execute(query)

        cities = [row[0] for row in cursor.fetchall()]

        return cities

    except Exception as e:

        logger.exception("Failed to fetch city list.")

        return []

    finally:

        cursor.close()
        connection.close()


def get_weather_condition_distribution(city=None, start_date=None, end_date=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        weather_condition,
        COUNT(*) AS total
    FROM weather_data
    WHERE 1=1
    """

    values = []

    if city and city != "All Cities":
        query += " AND city = %s"
        values.append(city)

    if start_date and end_date:
        query += " AND DATE(fetched_at) BETWEEN %s AND %s"
        values.extend([start_date, end_date])

    query += """
    GROUP BY weather_condition
    ORDER BY total DESC
    """

    try:

        logger.info(
            f"Fetching weather condition distribution | City: {city}, Start: {start_date}, End: {end_date}"
        )

        cursor.execute(query, tuple(values))

        return cursor.fetchall()

    except Exception as e:

        logger.exception("Failed to fetch weather condition distribution.")

        return []

    finally:

        cursor.close()
        connection.close()

def get_city_temperature_comparison(start_date=None, end_date=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        city,
        ROUND(AVG(temperature),2) AS avg_temperature
    FROM weather_data
    WHERE 1=1
    """

    values = []

    if start_date and end_date:
        query += " AND DATE(fetched_at) BETWEEN %s AND %s"
        values.extend([start_date, end_date])

    query += """
    GROUP BY city
    ORDER BY avg_temperature DESC
    """

    try:

        logger.info(
            f"Fetching city temperature comparison | Start: {start_date}, End: {end_date}"
        )

        cursor.execute(query, tuple(values))

        return cursor.fetchall()

    except Exception as e:

        logger.exception("Failed to fetch city temperature comparison.")

        return []

    finally:

        cursor.close()
        connection.close()

def predict_weather_by_city(city):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        logger.info(f"Predicting weather for {city}")

        query = """
        SELECT
            city,
            temperature,
            humidity,
            pressure,
            wind_speed,
            weather_condition,
            fetched_at
        FROM weather_data
        WHERE city = %s
        ORDER BY fetched_at
        """

        cursor.execute(query, (city,))

        data = cursor.fetchall()

        if not data:

            logger.warning(f"No historical data found for {city}")

            return None

        import pandas as pd

        df = pd.DataFrame(data)

        latest = df.iloc[-1]

        summary = (
            df.groupby("weather_condition")
            .agg(
                average_temperature=("temperature", "mean"),
                average_humidity=("humidity", "mean"),
                average_pressure=("pressure", "mean"),
                average_wind_speed=("wind_speed", "mean")
            )
            .reset_index()
        )

        best_match = None
        smallest_difference = float("inf")

        for _, row in summary.iterrows():

            temp_difference = abs(
                latest["temperature"] -
                row["average_temperature"]
            )

            humidity_difference = abs(
                latest["humidity"] -
                row["average_humidity"]
            )

            pressure_difference = abs(
                latest["pressure"] -
                row["average_pressure"]
            )

            wind_difference = abs(
                latest["wind_speed"] -
                row["average_wind_speed"]
            )

            weighted_difference = (
                temp_difference * 0.4 +
                humidity_difference * 0.3 +
                pressure_difference * 0.2 +
                wind_difference * 0.1
            )

            if weighted_difference < smallest_difference:

                smallest_difference = weighted_difference

                best_match = {

                    "weather_condition": row["weather_condition"],

                    "average_temperature": row["average_temperature"],

                    "average_humidity": row["average_humidity"],

                    "average_pressure": row["average_pressure"],

                    "average_wind_speed": row["average_wind_speed"],

                    "score": weighted_difference
                }

        logger.info(f"Prediction completed for {city}")

        return {

            "latest": latest,

            "prediction": best_match

        }

    except Exception:

        logger.exception("Prediction failed.")

        return None

    finally:

        cursor.close()

        connection.close()