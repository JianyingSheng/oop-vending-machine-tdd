"""
test_vending_machine.py
"""
import pytest
import vending_machine

def test_insert_coin_reject_not_coin_class():
    """
    test if insert integer will raise ValueError
    """
    machine = vending_machine.VendingMachine()
    with pytest.raises(ValueError):
        machine.insert_coin(25)
