from shopping_cart import ShoppingCart
import pytest

# Setting up the max amount of items allowed in basket
# by using pytest fixtures
# Good for initialisation.
@pytest.fixture
def cart():
    # all set up for cart here
    return ShoppingCart(5)

def test_can_add_item_to_cart():
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item():
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail():
    # adding max amount of items
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        # attempting to add over the max amount
        cart.add("mango")


def test_can_get_total_price():
    cart.add("apple")
    cart.add("orange")
    price_map = {"apple": 1.0, "orange": 2.0}
    assert cart.get_total_price(price_map) == 3.0

