from datetime import date

from shop.discounts import apply_discount


def test_welcome_code():
    assert apply_discount(1000, "welcome10", today=date(2026, 1, 1)) == 900
