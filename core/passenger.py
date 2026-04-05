# passenger.py

from core.utils import get_positive_int, get_non_negative_float


def get_passenger_count():
    """
    Returns number of passengers (must be > 0)
    """
    return get_positive_int("Enter number of passengers: ")


def get_passenger_details(index):
    """
    Collects details for a single passenger
    """
    print(f"\n--- Passenger {index + 1} ---")

    age = get_positive_int("Enter age: ")
    baggage = get_non_negative_float("Enter baggage weight (kg): ")

    return {
        "age": age,
        "baggage": baggage
    }


def collect_passengers():
    """
    Collects all passenger data and returns a list
    """
    passengers = []

    count = get_passenger_count()

    for i in range(count):
        passenger = get_passenger_details(i)
        passengers.append(passenger)

    return passengers