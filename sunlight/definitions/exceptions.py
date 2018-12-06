class SunlightServiceException(Exception):
    """Base exception for sunlight service exceptions."""


class InvalidIanaTimezoneError(SunlightServiceException):
    """Exception raised upon encountering an invalid iana timezone."""
