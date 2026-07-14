# 🌦️ Weather Analytics Dashboard

A Weather Analytics Dashboard built using **Python, Streamlit, MySQL, Docker, and WeatherAPI**.

The application fetches live weather data from WeatherAPI, stores it in a MySQL database, and provides interactive dashboards, analytics, insights, and weather predictions.

---

# Features

## Current Weather
- Fetch live weather data for any city
- Display current weather information
- Save weather data into MySQL database

## Weather History
- View all previously fetched weather records
- Search weather history by city
- Filter data using date range

## Analytics Dashboard
- Dashboard statistics
- Temperature trend
- Humidity trend
- Wind speed trend
- Weather condition distribution
- Average temperature comparison across cities
- CSV export

## Insights
- Temperature vs Humidity analysis
- Correlation analysis
- Correlation heatmap
- Scatter plot visualization
- Weather condition analysis
- Historical weather prediction
- Trend detection
- Outlier detection using IQR

## Engineering Features
- Logging
- Exception Handling
- Unit Testing using Pytest
- Docker Support

---

# Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- MySQL

### API
- WeatherAPI

### Libraries
- Pandas
- Plotly
- Requests
- mysql-connector-python
- python-dotenv
- Pytest

### DevOps
- Docker
- Docker Compose

---

# Project Structure

```text
Weather-App/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env
│
├── database/
│   └── db.py
│
├── services/
│   ├── weather_api.py
│   └── weather_service.py
│
├── pages/
│   ├── current_weather.py
│   ├── search_history.py
│   ├── weather_history.py
│   ├── analytics.py
│   └── insights.py
│
├── utils/
│   └── logger.py
│
├── logs/
│
└── tests/
    ├── test_db.py
    └── test_weather_api.py
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Weather-App
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root
DB_NAME=weather_tracker

WEATHER_API_KEY=YOUR_API_KEY
```

---

# Run the Project

```bash
streamlit run app.py
```

Application:

```
http://localhost:8501
```

---

# Running with Docker

Build Docker Image

```bash
docker compose build
```

Start Containers

```bash
docker compose up
```

Stop Containers

```bash
docker compose down
```

---

# Database

The application automatically creates the required table if it does not already exist.

Database:

```
weather_tracker
```

Table:

```
weather_data
```

---

# Testing

Run all unit tests.

```bash
python -m pytest
```

---

# Logging

Application logs are stored in the `logs` directory.

Logging is implemented for:

- Database operations
- API requests
- Analytics
- Exception handling

---

# Screenshots

Add screenshots of:

- Current Weather
- Weather History
- Analytics Dashboard
- Insights Page

---

# Future Enhancements

- Machine Learning based weather prediction
- Cloud deployment
- User Authentication
- Scheduled weather updates
- Email notifications

- CI/CD using GitHub Actions
- Automated scheduled weather collection
- Interactive map visualization

---

# Author

**Aroosh Reddy**

Weather Analytics Dashboard Project