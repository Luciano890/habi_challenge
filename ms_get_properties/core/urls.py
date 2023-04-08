"""URL Configuration for ms_get_properties."""
from app import APIApp
from .views import get_all_properties_available_to_users

router = APIApp()

router.path(get_all_properties_available_to_users, "/properties/available-to-users/")
