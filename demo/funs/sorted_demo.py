nums = [10, -11, -24, 55, 6]

for n in sorted(nums, key=abs):
    print(n)

names = ['Abc', 'Pqrs', 'Dddeef', 'Xy']

for n in sorted(names, key=lambda v: v[-1],reverse=True):
    print(n)
