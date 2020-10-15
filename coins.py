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

@dataclass
class Dime(Coin):
    """
    child class extended from coin
    """
    value: int = 10
    label: str = "10"+u'\xa2'
@dataclass
class Quarter(Coin):
    """
    child class extended from coin
    """
    value: int = 25
    label: str = "25"+u'\xa2'
@dataclass
class Loonie(Coin):
    """
    child class extended from coin
    """
    value: int = 100
    label: str = '$1'
@dataclass
class Toonie(Coin):
    """
    child class extended from coin
    """
    value: int = 200
    label: str = '$2'
