class Marks_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.data):
            raise StopIteration
        else:
            self.pos += 1
            return self.data[self.pos - 1]


class Marks:
    def __init__(self):
        self.marks = [20, 30, 40, 25, 66]

    def __iter__(self):
        return Marks_Iterator(self.marks)


m = Marks()
mi = iter(m)
print(next(mi))
print(next(mi))

mi2 = iter(m)
print(next(mi2))
print(next(mi2))

for v in m:
    print(v)

print(sum(m))
