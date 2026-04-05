# booking.py

from core.routes import get_distance, get_all_cities, is_valid_route
from core.constants import TRAIN_TYPES, CLASSES
from core.passenger import collect_passengers
from core.fare import calculate_total_fare
from core.promo import apply_promo, get_promo_code
from core.utils import get_valid_choice, get_non_empty_string


def select_route():
    """
    Handles route selection
    """
    cities = get_all_cities()

    print("\nAvailable Cities:")
    for city in cities:
        print("-", city)

    while True:
        source = get_non_empty_string("Enter source city: ")
        destination = get_non_empty_string("Enter destination city: ")

        if is_valid_route(source, destination):
            distance = get_distance(source, destination)
            return source.title(), destination.title(), distance
        else:
            print("Invalid route! Please try again.")


def select_train_type():
    """
    Displays train menu and returns choice
    """
    print("\nSelect Train Type:")
    for key, value in TRAIN_TYPES.items():
        print(f"{key}. {value['name']}")

    choice = get_valid_choice("Enter choice: ", list(TRAIN_TYPES.keys()))
    return choice


def select_class():
    """
    Displays class menu and returns choice
    """
    print("\nSelect Travel Class:")
    for key, value in CLASSES.items():
        print(f"{key}. {value['name']}")

    choice = get_valid_choice("Enter choice: ", list(CLASSES.keys()))
    return choice


def create_booking():
    """
    Main booking workflow
    """

    print("\n===== Railway Ticket Booking =====")

    # Step 1: Route selection
    source, destination, distance = select_route()

    # Step 2: Train type
    train_choice = select_train_type()

    # Step 3: Class
    class_choice = select_class()

    # Step 4: Passenger data
    passengers = collect_passengers()

    # Context for fare calculation
    context = {
        "distance": distance,
        "train_choice": train_choice,
        "class_choice": class_choice
    }

    # Step 5: Calculate fares
    individual_fares = []
    subtotal = 0

    for i, passenger in enumerate(passengers):
        fare = calculate_total_fare(passenger, context)
        individual_fares.append(fare)
        subtotal += fare

    # Step 6: Promo
    print(f"\nSubtotal: ₹{round(subtotal, 2)}")
    code = get_promo_code()
    final_total = apply_promo(subtotal, code)

    # Step 7: Summary
    summary = {
        "source": source,
        "destination": destination,
        "distance": distance,
        "train": TRAIN_TYPES[train_choice]["name"],
        "class": CLASSES[class_choice]["name"],
        "passengers": passengers,
        "individual_fares": individual_fares,
        "subtotal": round(subtotal, 2),
        "final_total": final_total
    }

    return summary