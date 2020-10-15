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

def test_dime_value_10():
    """
    test child class Dime of Coin value is 10
    """
    coin = coins.Dime()
    assert coin.value == 10

def test_dime_str_label():
    """
    test dime child class of Coin label is 10¢
    """
    coin = coins.Dime()
    assert str(coin) == '10¢'
def test_quarter_value_25():
    """
    test child class quarter of Coin value is 25
    """
    coin = coins.Quarter()
    assert coin.value == 25

def test_quarter_str_label():
    """
    test quarter child class of Coin label is 25¢
    """
    coin = coins.Quarter()
    assert str(coin) == '25¢'

def test_loonie_value_100():
    """
    test child class loonie of Coin value is 100
    """
    coin = coins.Loonie()
    assert coin.value == 100

def test_loonie_str_label():
    """
    test loonie child class of Coin label is $1
    """
    coin = coins.Loonie()
    assert str(coin) == '$1'

def test_toonie_value_200():
    """
    test child class toonie of Coin value is 200
    """
    coin = coins.Toonie()
    assert coin.value == 200

def test_toonie_str_label():
    """
    test  toonie child class of Coin label is $2
    """
    coin = coins.Toonie()
    assert str(coin) == '$2'
