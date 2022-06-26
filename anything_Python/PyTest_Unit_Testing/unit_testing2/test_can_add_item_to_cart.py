from shopping_cart import ShoppingCart


def test_an_add_item_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    assert cart.size() == 1
