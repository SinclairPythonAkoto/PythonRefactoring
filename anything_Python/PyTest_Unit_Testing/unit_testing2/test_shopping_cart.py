from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock
import pytest

# Setting up the max amount of items allowed in basket
# by using pytest fixtures
# Good for initialisation.
@pytest.fixture
def cart():
    # all set up for cart here
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    # adding max amount of items
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        # attempting to add over the max amount
        cart.add("mango")


def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    # mock to return a value dependant on the value of apple/fruit
    # you can add additional mocks, add more fruits or change values
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0
