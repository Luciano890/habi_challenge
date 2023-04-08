"""Test the endpoint."""
import pytest

from common.codes import OkCodes
from core.views import get_all_properties_available_to_users

def test_get_all_properties_available_to_users_type():
    """Test the type of the response."""
    assert isinstance(get_all_properties_available_to_users(), dict)

def test_get_all_properties_available_to_users_length():
    """Test the length of the response."""
    assert len(get_all_properties_available_to_users()) == 2

def test_get_all_properties_available_to_users_code():
    """Test the code of the response."""
    assert get_all_properties_available_to_users(
        operator="and"
    ).get("code") == OkCodes.GET_AVAILABLE_PROPERTIES_OK.value

def test_get_all_properties_status_not_available():
    """Test the response when the status is not available."""
    assert get_all_properties_available_to_users(
        status=1, operator="and"
    ).get("response") == []

@pytest.mark.parametrize(
    "input_city, input_year, input_operator, expected",
    [
        (
            "bogota",
            2018,
            "and",
            {
                "response": [
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": 5
                    },
                    {
                        "address": "diagonal 23 #28-21e",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": 4
                    }
                ],
                "code": OkCodes.GET_AVAILABLE_PROPERTIES_OK.value
            }
        ),
        (
            "bucaramanga",
            2021,
            "and",
            {
                "response": [
                    {
                        "address": "Cll 1A #11B",
                        "city": "bucaramanga",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2021,
                        "status": 4
                    }
                ],
                "code": OkCodes.GET_AVAILABLE_PROPERTIES_OK.value
            }
        )
    ]
)
def test_get_all_properties_available_to_users_params_city_and_year(
    input_city: str,
    input_year: int,
    input_operator: str,
    expected: dict,
):
    """Test the response when the city and year are filters."""
    assert get_all_properties_available_to_users(
        city=input_city, year=input_year, operator=input_operator
    ) == expected

@pytest.mark.parametrize(
    "input_city, input_status, input_operator, expected",
    [
        (
            "bucaramanga",
            4,
            "and",
            {
                "response": [
                    {
                        "address": "Cll 1A #11B",
                        "city": "bucaramanga",
                        "price": 300000000,
                        "description": "hermoso acabado, listo para estrenar super comodo",
                        "year": 2021,
                        "status": 4
                    }
                ],
                "code": OkCodes.GET_AVAILABLE_PROPERTIES_OK.value
            }
        ),
        (
            "bogota",
            5,
            "and",
            {
                "response": [
                    {
                        "address": "diagonal 23 #28-21",
                        "city": "bogota",
                        "price": 270000000,
                        "description": "Apartamento con hermosas vistas",
                        "year": 2018,
                        "status": 5
                    }
                ],
                "code": OkCodes.GET_AVAILABLE_PROPERTIES_OK.value
            }
        )
    ]
)
def test_get_all_properties_available_to_users_params_city_and_status(
    input_city: str,
    input_status: str,
    input_operator: str,
    expected: dict,
):
    """Test the response when the city and status are filters."""
    assert get_all_properties_available_to_users(
        city=input_city, status=input_status, operator=input_operator
    ) == expected
