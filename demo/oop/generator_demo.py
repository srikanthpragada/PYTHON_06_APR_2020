def numbers():
    for n in range(1, 11):
        print("In numbers()")
        yield n


g = numbers()
print(type(g))

#
print(next(g))
print(next(g))
#
# for n in g:
#     print(n, end = ' ')