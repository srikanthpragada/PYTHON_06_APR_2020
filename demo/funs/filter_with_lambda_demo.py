nums = [10, 11, 24, 55, 6]

for n in filter(lambda v : v % 2 == 0, nums):
    print(n)

names = ['Abc','Pqrs','Dddeef','Xy']

for n in filter(lambda s : len(s) > 3, names):
    print(n)



