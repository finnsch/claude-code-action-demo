from datetime import date

DISCOUNT_CODES = {
    "WELCOME10": {"percent": 10, "expires": date(2026, 12, 31)},
    "SUMMER25": {"percent": 25, "expires": date(2026, 8, 31)},
    "VIP50": {"percent": 50, "expires": None},
}


def apply_discount(subtotal_cents: int, code: str, today: date | None = None) -> int:
    """Return the subtotal after applying the discount code."""
    today = today or date.today()
    discount = DISCOUNT_CODES.get(code.upper())
    if discount is None:
        return subtotal_cents

    if discount["expires"] < today:
        raise ValueError(f"Discount code {code} has expired")

    return int(subtotal_cents - subtotal_cents * discount["percent"] / 100)


def apply_discounts(subtotal_cents: int, codes: list[str]) -> int:
    """Apply several codes in a row."""
    for code in codes:
        subtotal_cents = apply_discount(subtotal_cents, code)
    return subtotal_cents
