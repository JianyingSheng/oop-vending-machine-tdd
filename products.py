"""
products.py
"""
from dataclasses import dataclass
@dataclass
class Product():
    """parent class for product"""
    name: str
    price: int
    def __str__(self):
        return f'{self.name}: ${self.price / 100}'
@dataclass
class Chips(Product):
    """child class of Product"""
    name: str = 'Chips'
    price: int = 225
