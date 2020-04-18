# Module with numeric functions


def iseven(n):
    return n % 2 == 0


def isleapyear(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


if __name__ == '__main__':
    print("Testing")
    print(iseven(11))
    print(isleapyear(2020))
else:
    print("Importing module", __name__)
