"""
test_coins.py
"""
import coins

def test_nickel_value_5():
    """
    test child class Nickel of Coin value is 5
    """
    coin = coins.Nickel()
    assert coin.value == 5

def test_nickel_str_label():
    """
    test child class of Coin label is 5¢
    """

    coin = coins.Nickel()
    assert str(coin) == '5¢'
