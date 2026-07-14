import os
import mysql.connector
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()


def get_connection():

    try:

        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        logger.info("Connected to MySQL database.")

        return connection

    except Exception as e:

        logger.exception("Failed to connect to MySQL database.")

        return None


def create_table():

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(100),
        country VARCHAR(100),
        latitude FLOAT,
        longitude FLOAT,
        temperature FLOAT,
        humidity INT,
        pressure FLOAT,
        wind_speed FLOAT,
        weather_condition VARCHAR(100),
        fetched_at DATETIME
    )
    """

    try:

        cursor.execute(create_table_query)

        connection.commit()

        logger.info("weather_data table verified/created successfully.")

    except Exception as e:

        logger.exception("Failed to create weather_data table.")

    finally:

        cursor.close()
        connection.close()