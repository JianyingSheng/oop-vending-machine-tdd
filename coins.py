"""
coins.py
"""
from dataclasses import dataclass

@dataclass
class Coin:
    """
    parent class for coin
    """
    value: int
    label: str
    def __str__(self):
        return self.label

@dataclass
class Nickel(Coin):
    """
    child class extended from coin
    """
    value: int = 5
    label: str = "5"+u'\xa2'
