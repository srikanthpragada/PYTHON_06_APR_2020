def fun(a):
    pass


first = fun
print(type(fun), id(fun))


def fun(a, b):
    pass


print(type(fun), id(fun))

first(10)
fun(10, 20)
