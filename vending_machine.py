"""
vending_machine.py
"""
from dataclasses import dataclass,field
import coins

@dataclass
class VendingMachine():
    """
    Vending machine class
    """
    insert_coins: list = field(default_factory=list)
    purchases: list = field(default_factory = list)
    def insert_coin(self, coin):
        """
        insert coin to the vending machine
        """
        if not isinstance(coin,coins.Coin):
            raise ValueError
        self.insert_coins.append(coin)
        return self.insert_coins
