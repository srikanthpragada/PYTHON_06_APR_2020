def fun(a, b, *nums):
    pass


def wishing(*names, message='Hi'):
    for n in names:
        print(message, n)


wishing('Tom', 'Hank')
wishing('John', message="Hello")

fun(10, 20, 30, 40)
