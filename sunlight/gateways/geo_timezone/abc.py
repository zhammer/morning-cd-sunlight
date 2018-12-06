from abc import ABC, abstractmethod

from sunlight.definitions import Coordinates


class GeoTimezoneGatewayABC(ABC):

    @abstractmethod
    def fetch_timezone_coordinates(self, iana_name: str) -> Coordinates:
        ...
