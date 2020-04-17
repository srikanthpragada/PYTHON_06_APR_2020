nums = [10, -11, -24, 55, 6]

for n in sorted(nums, key=abs):
    print(n)

names = ['Abc', 'Pqrs', 'Dddeef', 'Xy']

for n in sorted(names, key=lambda v: v[-1], reverse=True):
    print(n)

# Sorting a dict by values

players = {'A': 20, 'C': 30, 'B': 45, 'E': 23, 'D': 31}

for n, a in sorted(players.items(), key=lambda t: t[1]):
    print(n, a)

