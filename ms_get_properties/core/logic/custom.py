"""Custom logic to connect with database."""
from dataclasses import dataclass
from typing import Callable

from common.codes import OkCodes
from common.enums import TablesDataBase
from common.helpers import PROPERTY_DATA, QUERY_FILTERS

@dataclass(frozen=True)
class CustomLogic:
    """CustomLogic class.

    Attributes:
        * cursor (Callable): Cursor to execute queries.
        * database (str): Database name.

    Methods:
        * _remove_not_allowed_status(self, data: list[dict], /) -> list[dict]:
            Remove not allowed status from data.
        * _serializable_response(
            self, *, response: list, code: int
        ) -> dict[str, list[dict] | int]:
            Serialize response.
        * get_all_available_properties(self, **params: dict) -> dict[str, list[dict] | int]:
            Get all rows from a table by params.
    """
    cursor: Callable
    database: str

    def _remove_not_allowed_status(self, data: list[dict], /) -> list[dict]:
        """Remove not allowed status from data.

        Parameters:
            * data (list[dict]): Data to remove not allowed status.

        Returns:
            * list[dict]: Data without allowed status.
        """
        return [row for row in data if row.get("status") in (3, 4, 5)]

    def _serializable_response(
        self, *, response: list, code: int
    ) -> dict[str, list[dict] | int]:
        """Serialize response.
        
        Parameters:
            * response (list): Response to serialize.
            * code (int): Code response.
            
        Returns:
            * dict[str, list[dict] | int]: Serialized response.
        """
        return {
            "response": self._remove_not_allowed_status(
                [
                    dict(zip(PROPERTY_DATA, data))
                    for data in response
                ]
            ),
            "code": code,
        }

    def get_all_available_properties(self, **params: dict) -> dict[str, list[dict] | int]:
        """Get all rows from a table by params.
        
        Parameters:
            * params (dict): Params to filter the query.
            
        Returns:
            * dict: Response with all rows from a table.
        """
        properties = self.database + "." + TablesDataBase.PROPERTIES.value
        status = self.database + "." + TablesDataBase.STATUS.value
        status_history = self.database + "." + TablesDataBase.STATUS_HISTORY.value
        query = f"""
        SELECT p.address, p.city, p.price, p.description, p.year, sh.status_id
        FROM {properties} p
        JOIN (
            SELECT sh.*
            FROM {status_history} sh
            JOIN (
            SELECT property_id, MAX(update_date) AS max_date
            FROM {status_history}
            GROUP BY property_id
            ) last_status
            ON sh.property_id = last_status.property_id AND sh.update_date = last_status.max_date
        ) sh ON p.id = sh.property_id 
        WHERE sh.status_id IN (
            SELECT id FROM {status} WHERE name IN ('pre_venta', 'en_venta', 'vendido')    
        ) AND p.address != ''
        """
        query_operator = QUERY_FILTERS.get(params.get("operator"), "and")
        for param, value in params.items():
            if value and param in query_operator:
                query += query_operator.get(param).format(**params)
        self.cursor.execute(query)
        return self._serializable_response(
            response=self.cursor,
            code=OkCodes.GET_AVAILABLE_PROPERTIES_OK.value
        )
