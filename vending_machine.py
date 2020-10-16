"""
vending_machine.py
"""
from dataclasses import dataclass,field
import coins
import products

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

    def buy_product(self, product):
        """
        buy product from vending machine
        """
        if not isinstance(product,products.Product):
            raise ValueError
        if self.get_balance() < product.price :
            raise InsufficientFunds
        self.purchases.append(product)
        return self.purchases

    def get_balance(self):
        """
        get balance before or after purchasing product
        """
        balance = 0
        for coin in self.insert_coins:
            balance += coin.value
        for product in self.purchases:
            balance -= product.price
        return balance

    def get_change(self):
        """
        method to return change, larger coin value first
        """
        coins_list = [coins.Toonie(),coins.Loonie(),coins.Quarter(),
                      coins.Dime(), coins.Nickel()]
        list_changes = []
        temp = self.get_balance()
        temp -= temp % 5
        while temp > 0:
            for coin in coins_list:
                if temp % coin.value == 0:
                    list_changes.append(coin)
                    temp -= coin.value
                    break
        return sorted(list_changes,key=lambda customer:customer.value, reverse=True)

class InsufficientFunds(Exception):
    """
    indicate that there is not insufficient funds to make purchases
    """
