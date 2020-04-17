import sys

number = int(sys.argv[1])

for i in range(1, 11):
    print(f"{number:3} * {i:2} = {i * number:5}")
