def zero(v):
    print(id(v))
    v = 0
    print(id(v), v)


a = 100
print(id(a))
zero(a)
print(a)
