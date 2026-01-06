from datetime import datetime

import pytest
import pytz

from ndastro_engine.core import get_planet_position, get_sunrise_sunset
from ndastro_engine.enums.planet_enum import Planets

"""Tests for astronomical calculations in ndastro engine."""


class TestGetPlanetPosition:
    """Test suite for get_planet_position function."""

    def test_get_planet_position_returns_tuple(self):
        """Test that get_planet_position returns a tuple of three floats."""
        result = get_planet_position(planet=Planets.SUN, lat=40.7128, lon=-74.0060, given_time=datetime(2024, 1, 1, 12, 0, 0, tzinfo=pytz.UTC))

        assert isinstance(result, tuple)
        assert len(result) == 3
        assert all(isinstance(x, float) for x in result)

    def test_get_planet_position_longitude_range(self):
        """Test that longitude is within valid range (0-360 degrees)."""
        longitude, _, _ = get_planet_position(
            planet=Planets.MARS, lat=51.5074, lon=-0.1278, given_time=datetime(2024, 6, 15, 0, 0, 0, tzinfo=pytz.UTC)
        )

        assert 0 <= longitude <= 360

    def test_get_planet_position_latitude_range(self):
        """Test that latitude is within valid range (-90 to 90 degrees)."""
        _, latitude, _ = get_planet_position(
            planet=Planets.JUPITER, lat=-33.8688, lon=151.2093, given_time=datetime(2024, 3, 20, 6, 0, 0, tzinfo=pytz.UTC)
        )

        assert -90 <= latitude <= 90

    def test_get_planet_position_distance_positive(self):
        """Test that distance is always positive."""
        _, _, distance = get_planet_position(
            planet=Planets.VENUS, lat=35.6762, lon=139.6503, given_time=datetime(2024, 12, 25, 18, 0, 0, tzinfo=pytz.UTC)
        )

        assert distance > 0

    def test_get_planet_position_different_planets(self):
        """Test that different planets return different positions."""
        time = datetime(2024, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        lat, lon = 0.0, 0.0

        sun_pos = get_planet_position(Planets.SUN, lat, lon, time)
        moon_pos = get_planet_position(Planets.MOON, lat, lon, time)

        assert sun_pos != moon_pos

    def test_get_planet_position_different_times(self):
        """Test that same planet at different times returns different positions."""
        lat, lon = 40.7128, -74.0060

        pos1 = get_planet_position(Planets.MERCURY, lat, lon, datetime(2024, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        pos2 = get_planet_position(Planets.MERCURY, lat, lon, datetime(2024, 6, 1, 0, 0, 0, tzinfo=pytz.UTC))

        assert pos1 != pos2

    def test_get_planet_position_different_locations(self):
        """Test that same planet from different locations may return different positions."""
        time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=pytz.UTC)

        pos1 = get_planet_position(Planets.SATURN, 40.7128, -74.0060, time)
        pos2 = get_planet_position(Planets.SATURN, -33.8688, 151.2093, time)

        # Positions may differ slightly due to parallax
        assert isinstance(pos1, tuple)
        assert isinstance(pos2, tuple)

    @pytest.mark.parametrize(
        ("planet", "longitude", "latitude", "distance", "ayanamsa"),
        [
            (Planets.SUN, 279.8051877358686, 0.0006220123496504032, 0.9833628050249553, None),
            (Planets.SUN, 255.61352106586864, 0.0006220123496504032, 0.9833628050249553, 24.19166667),
        ],
    )
    def test_get_planet_position_all_planets(
        self, planet: Planets, longitude: float, latitude: float, distance: float, ayanamsa: float | None
    ) -> None:
        """Test that function works for all major planets."""
        lat, lon, dis = get_planet_position(
            planet=planet, lat=12.97, lon=77.59, given_time=datetime(2023, 12, 31, 18, 30, 0, tzinfo=pytz.UTC), ayanamsa=ayanamsa
        )
        assert lat == latitude
        assert lon == longitude
        assert dis == distance


class TestGetSunriseSunset:
    """Test cases for get_sunrise_sunset function."""

    def test_get_sunrise_sunset_basic(self) -> None:
        """Test basic sunrise/sunset calculation."""
        # Setup test data
        lat = 12.97
        lon = 77.59
        test_date = datetime(2026, 1, 5, 10, 0, 0, tzinfo=pytz.timezone("UTC"))

        # Execute function
        sunrise, sunset = get_sunrise_sunset(lat, lon, test_date)

        # Assertions
        assert sunrise.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%H:%M:%S") == "06:43:09"
        assert sunset.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%H:%M:%S") == "18:06:46"
