# promo.py

from core.constants import PROMO_CODES


def apply_promo(subtotal, code):
    """
    Applies promo code to subtotal.
    Returns final total after discount.
    """

    if not code:
        return subtotal  # No promo applied

    code = code.strip().upper()

    if code not in PROMO_CODES:
        print("Invalid promo code! No discount applied.")
        return subtotal

    promo = PROMO_CODES[code]

    if promo["type"] == "percentage":
        discount = (promo["value"] / 100) * subtotal
        final_total = subtotal - discount

    elif promo["type"] == "flat":
        discount = promo["value"]
        final_total = subtotal - discount

        # Ensure total doesn't go below zero
        if final_total < 0:
            final_total = 0

    else:
        return subtotal  # safety fallback

    print(f"Promo applied: {code}")
    print(f"Discount: ₹{round(discount, 2)}")

    return round(final_total, 2)


def get_promo_code():
    """
    Prompts user for promo code (optional)
    """
    code = input("Enter promo code (or press Enter to skip): ")
    return code.strip()