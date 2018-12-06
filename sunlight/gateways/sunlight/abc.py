from abc import ABC, abstractmethod
from datetime import date

from sunlight.definitions import Coordinates, SunlightWindow


class SunlightGatewayABC(ABC):

    @abstractmethod
    def fetch_sunlight_window(self, coordinates: Coordinates, on_date: date) -> SunlightWindow:
        ...
