# routes.py

# Base route data (one direction only)
BASE_ROUTES = {
    ("New Delhi", "Mumbai"): 1460,
    ("New Delhi", "Kolkata"): 1525,
    ("New Delhi", "Chennai"): 2200,
    ("New Delhi", "Hyderabad"): 1670,
    ("Mumbai", "Kolkata"): 1970,
    ("Mumbai", "Chennai"): 1300,
    ("Mumbai", "Hyderabad"): 711,
    ("Kolkata", "Chennai"): 1200,
    ("Kolkata", "Hyderabad"): 1600,
    ("Chennai", "Hyderabad"): 633
}


# Create bidirectional routes automatically
ROUTES = {}

for (src, dest), dist in BASE_ROUTES.items():
    ROUTES[(src.lower(), dest.lower())] = dist
    ROUTES[(dest.lower(), src.lower())] = dist


def get_distance(source, destination):
    """
    Returns distance between two cities.
    Case-insensitive.
    """
    key = (source.lower(), destination.lower())
    return ROUTES.get(key, None)


def get_all_cities():
    """
    Returns a sorted list of all unique cities.
    """
    cities = set()
    for src, dest in ROUTES.keys():
        cities.add(src.title())
        cities.add(dest.title())
    return sorted(cities)


def is_valid_route(source, destination):
    """
    Checks if route exists.
    """
    return get_distance(source, destination) is not None