from typing import NamedTuple

from sunlight.gateways.geo_timezone import GeoTimezoneGatewayABC
from sunlight.gateways.sunlight import SunlightGatewayABC


class Context(NamedTuple):
    sunlight_gateway: SunlightGatewayABC
    geo_timezone_gateway: GeoTimezoneGatewayABC
