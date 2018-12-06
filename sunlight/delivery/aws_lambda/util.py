from sunlight.context import Context
from sunlight.gateways.geo_timezone import GeoTimezoneGateway
from sunlight.gateways.sunlight import SunriseSunsetApiGateway


def create_default_context() -> Context:
    return Context(
        geo_timezone_gateway=GeoTimezoneGateway(),
        sunlight_gateway=SunriseSunsetApiGateway()
    )
