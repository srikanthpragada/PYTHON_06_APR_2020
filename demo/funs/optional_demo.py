# With optional parameter
def hello(name= "Guest", message='Hello'):
    print(message, name)


hello('Bruce', 'Good Morning')
hello(message="Hi", name="Tom")
hello('Scott')
hello('Bill', message = "Good Bye")
hello()
