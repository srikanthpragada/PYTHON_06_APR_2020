
nums = set()   # Empty set

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break

    nums.add(n)


for n in sorted(nums):
    print(n)





