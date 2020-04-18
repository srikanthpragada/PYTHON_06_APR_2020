class Product:
    # Constructor
    def __init__(self, name, price=0):
        # Object Attributes
        self.name = name
        self.price = price

    # Methods
    def net_price(self):
        return self.price * 1.15


p1 = Product("Bose HeadPhones", 25000)
p2 = Product("iPhone 11")
print(p1.net_price())
