l = [1, 2, 3]

try:
    l.add(4)
except ValueError as ex:
    print('ValueError')
else:
    print("Success")
finally:
    print('Finally')

print("Over")
