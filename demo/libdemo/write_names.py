
f = open("names.txt","wt")

names = []
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

# Write names in sorted order to file
for name in sorted(names):
    f.write(name + '\n')

f.close()
