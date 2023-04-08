"""Properties views."""
from config.db import cursor
from settings import DB_SCHEMA
from ..logic.custom import CustomLogic

custom = CustomLogic(cursor, DB_SCHEMA)

def get_all_properties_available_to_users(
    city: str = None,
    year: int = None,
    status: int = None,
    operator: str = "and",
) -> dict[str, list[dict] | int]:
    """Get all properties enabled.
    
    Parameters:
        * city (str): City to filter the query.
        * price (int): Price to filter the query.
        * description (str): Description to filter the query.
        * year (int): Year to filter the query.
        * status (int): Status to filter the query.
        * operator (str): Operator to filter the query.
        
    Returns:
        * dict: Response with all properties enabled.
    """
    return custom.get_all_available_properties(
        city=city,
        year=year,
        status=status,
        operator=operator,
    )
