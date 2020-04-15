# a and b are keyword only arguments
def fun(x, *, a, b):
    pass


fun(10, a=10, b=20)
fun(x=10, a=20, b=30)
