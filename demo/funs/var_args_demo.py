def wishing(*names, message='Hi'):
    for n in names:
        print(message, n)


wishing('Tom', 'Hank')
wishing('John', message="Hello")
