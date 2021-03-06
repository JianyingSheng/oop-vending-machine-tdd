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

@dataclass
class Drink(Product):
    """child class of Product"""
    name: str = 'Drink'
    price: int = 275

@dataclass
class Candy(Product):
    """child class of Product"""
    name: str = 'Candy'
    price: int = 315
