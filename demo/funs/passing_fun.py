def math_op(op, a, b):
    return op(a, b)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(math_op(mul, 10, 20))
print(math_op(add, 10, 20))
