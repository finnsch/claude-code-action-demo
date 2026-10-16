import pytest

from shop.cart import Cart, Item

APPLE = Item("A1", "Apple", 50)
PEAR = Item("P1", "Pear", 75)


def test_subtotal():
    cart = Cart()
    cart.add(APPLE, 3)
    cart.add(PEAR)
    assert cart.subtotal_cents() == 225


def test_add_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        Cart().add(APPLE, 0)


def test_remove():
    cart = Cart()
    cart.add(APPLE)
    cart.remove("A1")
    assert cart.subtotal_cents() == 0
