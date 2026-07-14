import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("WeatherApp")

logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(
        "logs/weather_app.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)