class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        # print(self, other)
        return self.age > other.age


if __name__ == '__main__':
    p1 = Person("Scott", 25)
    p2 = Person("Tom", 35)
    print(p1 > p2)
    print(p1 < p2)
    p3 = Person("Scott", 25)
    print(p1 == p3)
    print(p1 != p2)
    print(p1)
