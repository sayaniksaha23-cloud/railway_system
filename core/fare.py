# fare.py

from core.constants import TRAIN_TYPES, CLASSES


# Step 1 — Slab Fare
def calculate_slab_fare(distance):
    fare = 100  # base fare

    if distance <= 100:
        fare += distance * 1.0
    elif distance <= 300:
        fare += (100 * 1.0) + ((distance - 100) * 0.8)
    else:
        fare += (100 * 1.0) + (200 * 0.8) + ((distance - 300) * 0.6)

    return fare


# Step 2 — Senior Citizen Discount
def apply_senior_discount(fare, age):
    if age > 60:
        return fare * 0.6  # 40% discount
    return fare


# Step 3 — Train Premium
def apply_train_premium(fare, train_choice):
    premium = TRAIN_TYPES[train_choice]["premium"]
    return fare * premium


# Step 4 — Class Premium
def apply_class_premium(fare, class_choice):
    multiplier = CLASSES[class_choice]["multiplier"]
    return fare * multiplier


# Step 5 — Excess Baggage Fee
def calculate_baggage_fee(weight, class_choice):
    free_limit = CLASSES[class_choice]["baggage"]

    if weight > free_limit:
        extra_weight = weight - free_limit
        return extra_weight * 15
    return 0


# Step 6 — Flat Surcharge
def apply_surcharge(fare, train_choice):
    surcharge = TRAIN_TYPES[train_choice]["surcharge"]
    return fare + surcharge


# Final Fare Calculation (ALL STEPS COMBINED)
def calculate_total_fare(passenger, context):
    """
    passenger = {"age": int, "baggage": float}
    context = {
        "distance": int,
        "train_choice": int,
        "class_choice": int
    }
    """

    distance = context["distance"]
    train_choice = context["train_choice"]
    class_choice = context["class_choice"]

    # Step 1
    fare = calculate_slab_fare(distance)

    # Step 2
    fare = apply_senior_discount(fare, passenger["age"])

    # Step 3
    fare = apply_train_premium(fare, train_choice)

    # Step 4
    fare = apply_class_premium(fare, class_choice)

    # Step 5 (separate addition)
    baggage_fee = calculate_baggage_fee(passenger["baggage"], class_choice)

    # Step 6
    fare = apply_surcharge(fare, train_choice)

    # Final
    total = fare + baggage_fee

    return round(total, 2)