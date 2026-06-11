#!/usr/bin/env python3

class CashRegister:
   def __init__(self, discount=0):
      self.total = 0
      self.items = []
      self.previous_transactions = []
      self.discount = 0

      self.discount = discount

   @property
   def discount(self):
      return self._discount
   
   @discount.setter
   def discount(self, value):
      if isinstance(value, int) and value >= 0:
         self._discount = value
      else:
         print("not valid discount")


   def add_item(self, title, price, quantity):
      self.total += price * quantity
      for _ in range(quantity):
         self.items.append(title)

   def apply_discount(self):
      if not self.discount:
         print("There is no discount to apply.")
         return
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount

      self.previous_transactions.pop()

   def void_last_transaction(self):
      if not self.previous_transactions:
         print("No transactions to void.")
         return
      last = self.previous_transactions.pop()
      self.total -= last["price"] * last["quantity"]

      item = last["item"]
      quantity = last["quantity"]

      for _ in range(quantity):
         if item in self.items:
            self.items.remove(item)
