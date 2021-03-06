"""
test_products.py
"""
import products

def test_chips_price():
    """test chips price"""
    chips = products.Chips()
    assert chips.price == 225
def test_chips_str():
    """test chips str"""
    chips = products.Chips()
    assert str(chips)== "Chips: $2.25"

def test_drink_price():
    """test drink price"""
    drink = products.Drink()
    assert drink.price == 275
def test_drink_str():
    """test drink str"""
    drink = products.Drink()
    assert str(drink)== "Drink: $2.75"

def test_candy_price():
    """test candy price"""
    candy = products.Candy()
    assert candy.price == 315
def test_candy_str():
    """test candy str"""
    candy = products.Candy()
    assert str(candy)== "Candy: $3.15"
