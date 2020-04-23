
total = 0
while True:
    try:
        num = int(input("Enter number [0 top stop] :"))
        if num == 0:
            break

        total += num
    except ValueError:
        print("Invalid input. Please enter a valid number!")

print("Total : ", total)