class Product:
    # class attributes
    taxrate = 15

    @staticmethod
    def set_taxrate(taxrate):
        if taxrate >= 0:
            Product.taxrate = taxrate

    # Create a dummy product object
    @classmethod
    def create(cls, name):
        return cls(name)

    # Constructor
    def __init__(self, name, price=0):
        # Object Attributes
        self.name = name
        self.price = price

    @property
    def netprice(self):
        return self.price + self.price * Product.taxrate / 100


p = Product.create("Dummy")  # Call classmethod
print(p.name, p.price)

p1 = Product("Bose HeadPhones", 25000)
# Product.taxrate = 20
Product.set_taxrate(17)
print(p1.netprice)    # Property
print(p1.__dict__)

p2 = Product("iPhone 11")
