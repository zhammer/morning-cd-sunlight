from datetime import date

from sunlight.context import Context
from sunlight.definitions import SunlightWindow


def get_sunlight_window(context: Context, iana_timezone: str, on_date: date) -> SunlightWindow:
    """Get the approximate sunlight window (sunrise and sunset utc datetimes) of an iana timezone
    (i.e.'Europe/Moscow') on a given date.
    """
    coordinates = context.geo_timezone_gateway.fetch_timezone_coordinates(iana_timezone)
    return context.sunlight_gateway.fetch_sunlight_window(coordinates, on_date)
