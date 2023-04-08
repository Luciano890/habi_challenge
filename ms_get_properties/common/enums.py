"""Enumerations for the ms_get_properties microservice."""
from enum import Enum

class HTTPStatus(int , Enum):
    """HTTP status codes."""
    HTTP_200_OK = 200
    HTTP_404_NOT_FOUND = 404

class TablesDataBase(str, Enum):
    """Tables in the database."""
    PROPERTIES = "property"
    STATUS = "status"
    STATUS_HISTORY = "status_history"
