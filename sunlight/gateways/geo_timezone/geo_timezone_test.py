from .geo_timezone import GeoTimezoneGateway


def test_can_ignore_extra_iana_prefix() -> None:
    gateway = GeoTimezoneGateway()
    assert (gateway.fetch_timezone_coordinates('America/Indiana/Indianapolis') ==
            gateway.fetch_timezone_coordinates('America/Indianapolis'))


def test_can_fetch_montreal() -> None:
    gateway = GeoTimezoneGateway()
    gateway.fetch_timezone_coordinates('America/Montreal')


def test_can_fetch_kolkata_as_calcutta() -> None:
    gateway = GeoTimezoneGateway()
    assert (gateway.fetch_timezone_coordinates('Asia/Kolkata') ==
            gateway.fetch_timezone_coordinates('Asia/Calcutta'))
