def iseven(n):
    return n % 2 == 0


nums = [10, 11, 24, 55, 6]

for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, "How Are You"):
    print(c)


for c in filter(len, "How Are You"):
    print(c)


