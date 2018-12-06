import iana_tz_coord

from sunlight.definitions import Coordinates, exceptions
from sunlight.gateways.geo_timezone import GeoTimezoneGatewayABC


class GeoTimezoneGateway(GeoTimezoneGatewayABC):

    def fetch_timezone_coordinates(self, iana_name: str) -> Coordinates:
        try:
            coordinates: iana_tz_coord.Coordinates = iana_tz_coord.get_coordinates(iana_name)
        except LookupError:
            raise exceptions.InvalidIanaTimezoneError(f'{iana_name} is not a known iana timezone.')

        return Coordinates(**coordinates._asdict())
