import os

tree = os.walk(r"c:\classroom\apr6\demo")

for (dirname, dirs, files) in tree:
    for file in files:
        if file.endswith('.py'):
            print(dirname + "\\" + file)
