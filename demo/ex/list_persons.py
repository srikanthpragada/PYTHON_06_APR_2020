from oop.person import Person

persons = [Person('Abc', 40), Person('Xyz', 30), Person('Pqr', 25)]

for p in sorted(persons): # uses __gt__() to compare objects
    print(p)

for p in sorted(persons, key=lambda p: p.name):
    print(p)
