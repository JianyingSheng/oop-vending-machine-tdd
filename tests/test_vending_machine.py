"""
test_vending_machine.py
"""
import pytest
import vending_machine
import coins
import products
from vending_machine import InsufficientFunds

def test_insert_coin_reject_not_coin_class():
    """
    test if insert integer will raise ValueError
    """
    machine = vending_machine.VendingMachine()
    with pytest.raises(ValueError):
        machine.insert_coin(25)
def test_insert_nickel():
    """
    test insert instance of Nickel
    """
    machine = vending_machine.VendingMachine()
    nickel = coins.Nickel()
    assert machine.insert_coin(nickel) == [nickel]

def test_insert_dime():
    """
    test insert instance of Dime
    """
    machine = vending_machine.VendingMachine()
    dime = coins.Dime()
    assert machine.insert_coin(dime) == [dime]

def test_insert_dime_nickel():
    """
    test insert coin appended right
    """
    machine= vending_machine.VendingMachine()
    dime = coins.Dime()
    nickel = coins.Nickel()
    machine.insert_coin(dime)
    machine.insert_coin(nickel)
    assert machine.insert_coins == [dime,nickel]

def test_get_balance_0():
    """
    test when no coins are inserted, and no purchases have been made,
    the balance should be zero
    """
    machine = vending_machine.VendingMachine()
    assert machine.get_balance() == 0

def test_get_balance_two_loonie_candy_75():
    """
    given that two toonies are inserted into the machine and a candy bar
     was purchased, the method should return 85.
    """
    machine = vending_machine.VendingMachine()
    toonie = coins.Toonie()
    candy = products.Candy()
    machine.insert_coin(toonie)
    machine.insert_coin(toonie)
    machine.buy_product(candy)
    assert machine.get_balance() == 85
    #there is a typo in README file
def test_buy_product_with_insufficient_funds():
    """
    test buy product with insufficient funds
    """
    machine = vending_machine.VendingMachine()
    dime = coins.Dime()
    nickel = coins.Nickel()
    machine.insert_coin(dime)
    machine.insert_coin(nickel)
    drink = products.Drink()
    with pytest.raises(InsufficientFunds):
        machine.buy_product(drink)
def test_buy_product_with_integer_product():
    """
    test buy product with string input
    """
    machine = vending_machine.VendingMachine()
    with pytest.raises(ValueError):
        machine.buy_product("not a product type")
def test_get_change_balance_0():
    """
    When the balance is 0, no quarters should be returned
    """
    machine = vending_machine.VendingMachine()
    assert machine.get_change() == []

def test_get_change_balance_25():
    """
    When the balance is 25, a quarter should be returned
    """
    machine = vending_machine.VendingMachine()
    quarter = coins.Quarter()
    machine.insert_coin(quarter)
    assert machine.get_change() == [quarter]

def test_get_change_balance_265():
    """
    When the balance is 265, a toonie, two quarters, a dime and a nickel should be returned
    """
    machine = vending_machine.VendingMachine()
    quarter = coins.Quarter()
    toonie = coins.Toonie()
    dime = coins.Dime()
    nickel = coins.Nickel()
    machine.insert_coin(quarter)
    machine.insert_coin(toonie)
    machine.insert_coin(quarter)
    machine.insert_coin(dime)
    machine.insert_coin(nickel)
    assert machine.get_change() == [toonie,quarter,quarter,dime,nickel]
