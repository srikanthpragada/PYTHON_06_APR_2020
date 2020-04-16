g = 100  # Global variable


def fun1():
    g = 1
    a = 200  # local variable
    print(a, g)

    def fun2():
        a = 10
        b = 300  # Local variable
        print(g, a, b)  # Global, Enclosing, Local

    fun2()
    print(a)


fun1()
