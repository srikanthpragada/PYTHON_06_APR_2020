# Place positive numbers on left and negative numbers on right

p_nums = []
n_nums = []
while True:
    n = int(input("Enter  a number [0 to stop] :"))
    if n == 0:
        break

    if n < 0:
        n_nums.append(n)
    else:
        p_nums.append(n)


print(p_nums + n_nums)


