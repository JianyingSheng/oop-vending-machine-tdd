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
