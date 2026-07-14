from services.weather_service import (
    save_weather,
    get_dashboard_stats,
    get_all_cities
)


def test_save_weather():
    weather = save_weather("Hyderabad")
    assert weather is not None

def test_dashboard_stats():
    stats = get_dashboard_stats()
    assert stats is not None
    assert "total_records" in stats


def test_get_all_cities():
    cities = get_all_cities()
    assert isinstance(cities, list)
    assert len(cities) > 0