# constants.py to store the constants that have been used throughout the prograam

TRAIN_TYPES = {
    1: {"name": "Superfast", "speed": 120, "premium": 1.5, "surcharge": 100},
    2: {"name": "Express", "speed": 110, "premium": 1.25, "surcharge": 50},
    3: {"name": "Fast Passenger", "speed": 90, "premium": 1.0, "surcharge": 0}
}
CLASSES = {
    1: {"name": "Sleeper", "multiplier": 1.0, "baggage": 20},
    2: {"name": "AC 3-Tier", "multiplier": 1.5, "baggage": 30},
    3: {"name": "AC 2-Tier", "multiplier": 2.0, "baggage": 40}
}

PROMO_CODES = {
    "ADG20": {"type": "percentage", "value": 20},
    "WINTER500": {"type": "flat", "value": 500}
}