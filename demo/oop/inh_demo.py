from abc import ABC, abstractmethod

# Abstract class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print(self):
        print(self.name)
        print(self.email)

    # Abstract method
    @abstractmethod
    def gettype(self):
        pass


class Player(Person):
    def __init__(self, name, email, game):
        super().__init__(name, email)
        self.game = game

    # Overriding
    def print(self):
        super().print()
        print(self.game)

    def gettype(self):
        return "Plays " + self.game


# p1 = Person("Abc", "abc@gmail.com")
# p1.print()

p2 = Player("Xyz", 'xyz@gmail.com', "Soccer")
p2.print()
