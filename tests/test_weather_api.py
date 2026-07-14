from services.weather_api import get_weather


def test_get_weather():
    weather = get_weather("Hyderabad")
    assert weather is not None
    assert weather["city"] == "Hyderabad"
    assert "temperature" in weather
    assert "humidity" in weather
    assert "pressure" in weather
    assert "wind_speed" in weather
    assert "weather_condition" in weather