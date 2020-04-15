# Positional only arguments
def fun(x, y, /):
    pass


def fun2(a, b):
    pass


fun(10, 20)
fun2(1, 2)
fun2(a=10, b=20)
x = 10
y = 20
fun2(x, y)
