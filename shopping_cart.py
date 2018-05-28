class ShoppingCart:

   items = {}
   def __init__(self, total = 0):
       self.total = total
   def add_item(self, item_name, quantity, price):
       self.item_name = item_name
       self.quantity = quantity
       self.price = price
       if not item_name in self.items:
           self.items[item_name] = quantity
       total = self.price*self.quantity + self.total
       self.items[self.item_name] = self.quantity

if __name__ =='__main__':
    john_cart = ShoppingCart()
    tom_cart = ShoppingCart()
    john_cart.add_item('milk', 2, 2.50)
    print "John's cart ->{}".format(john_cart.items)
    print "John's total ->{}".format(john_cart.total)
    print "Tom's cart ->{}".format(tom_cart.items)
