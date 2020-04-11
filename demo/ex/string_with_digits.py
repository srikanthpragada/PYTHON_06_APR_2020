# Count strings with at least one digit
count = 0
for i in range(5):
    s = input("Enter a string :")

    for c in s:
        if c.isdigit():
            count += 1
            break

print("Strings with digits :", count)
