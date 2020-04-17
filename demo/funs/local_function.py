g = 100  # Global variable


def fun1():
    global g
    g = 1
    a = 200  # local variable
    print(a, g)

    def fun2():
        nonlocal a
        a = 10
        b = 300  # Local variable
        print(g, a, b)  # Global, Enclosing, Local

    fun2()
    print(a)


fun1()
print(g)

