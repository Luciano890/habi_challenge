"""Helpers for ms_get_properties."""

PROPERTY_DATA: list[str] = [
    "address",
    "city",
    "price",
    "description",
    "year",
    "status",
]

QUERY_FILTERS: dict[str, str] = {
    "or": {
        "city": " OR p.city = '{city}'",
        "year": " OR p.year = {year}",
        "status": " OR sh.status_id = {status}",
    },
    "and": {
        "city": " AND p.city = '{city}'",
        "year": " AND p.year = {year}",
        "status": " AND sh.status_id = {status}",
    }
}
