"""
test_vending_machine.py
"""
import pytest
import vending_machine
import coins

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
    test insert coin append right
    """
    machine= vending_machine.VendingMachine()
    dime = coins.Dime()
    nickel = coins.Nickel()
    machine.insert_coin(dime)
    machine.insert_coin(nickel)
    assert machine.insert_coins == [dime,nickel]
