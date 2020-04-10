# take strings until end is given and display avg. length of strings

total = 0
count = 0

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    total += len(name)
    count += 1


print(f"Avg. Length = {total/count}")