# main.py

from core.booking import create_booking
from core.constants import TRAIN_TYPES

def display_summary(summary):
    """
    Displays final booking summary in a clean format
    """
    speed = None
    for key, val in TRAIN_TYPES.items():
      if val["name"] == summary["train"]:
        speed = val["speed"]

      if speed:
       time = summary["distance"] / speed
       print(f"Estimated Travel Time: {round(time, 2)} hours")
    

    print("\n========== BOOKING SUMMARY ==========")
    print(f"Route: {summary['source']} → {summary['destination']}")
    print(f"Distance: {summary['distance']} km")
    print(f"Train Type: {summary['train']}")
    print(f"Class: {summary['class']}")

    print("\n--- Passenger Details ---")
    for i, passenger in enumerate(summary["passengers"]):
        print(f"\nPassenger {i + 1}:")
        print(f"Age: {passenger['age']}")
        print(f"Baggage: {passenger['baggage']} kg")
        print(f"Fare: ₹{summary['individual_fares'][i]}")

    print("\n------------------------------")
    print(f"Subtotal: ₹{summary['subtotal']}")
    print(f"Final Total: ₹{summary['final_total']}")
    print("====================================")
    


def main():
    """
    Main program loop
    """

    print("Welcome to Railway Ticket Booking System")

    while True:
        summary = create_booking()
        display_summary(summary)

        choice = input("\nDo you want to make another booking? (y/n): ").strip().lower()

        if choice != 'y':
            print("Thank you for using the system!")
            break


if __name__ == "__main__":
    main()