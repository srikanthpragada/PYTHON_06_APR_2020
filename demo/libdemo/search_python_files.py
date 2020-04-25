import os

tree = os.walk(r"c:\classroom\apr6\demo")
search = "sys"


def file_contains_string(filename, searchstring):
    with open(filename) as f:
        if searchstring in f.read():
            return True
        else:
            return False


for (dirname, dirs, files) in tree:
    for file in files:
        if file.endswith('.py'):
            filename = dirname + "\\" + file
            if file_contains_string(filename, search):
                print(filename)
