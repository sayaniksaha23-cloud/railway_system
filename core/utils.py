# utils.py

def get_valid_int(prompt):
    """
    Keeps asking until user enters a valid integer.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_positive_int(prompt):
    """
    Ensures integer > 0
    """
    while True:
        value = get_valid_int(prompt)
        if value > 0:
            return value
        else:
            print("Value must be greater than 0.")


def get_non_negative_float(prompt):
    """
    Ensures float >= 0 (for baggage)
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Value cannot be negative.")
        except ValueError:
            print("Invalid input! Enter a number.")


def get_valid_choice(prompt, options):
    """
    Ensures user selects from given options (like menu)
    options = [1,2,3]
    """
    while True:
        choice = get_valid_int(prompt)
        if choice in options:
            return choice
        else:
            print(f"Invalid choice! Choose from {options}")


def get_non_empty_string(prompt):
    """
    Prevents empty input
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty.")


def normalize_string(value):
    """
    Standardizes input for comparison
    """
    return value.strip().lower()