def fun(**details):
    for k, v in details.items():
        print(k, v)


fun(a=10, b=20, msg="Hello")
