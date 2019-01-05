from .geo_timezone import GeoTimezoneGateway


def test_can_ignore_extra_iana_prefix() -> None:
    gateway = GeoTimezoneGateway()
    assert gateway.fetch_timezone_coordinates('America/Indiana/Indianapolis') == gateway.fetch_timezone_coordinates('America/Indianapolis')
