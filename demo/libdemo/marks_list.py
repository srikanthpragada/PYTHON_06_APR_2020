with open("marks.txt", "rt") as f:
    students = {}
    for line in f.readlines():
        parts = line.strip().split(',')
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = parts[1:]
        students[name] = sum(map(int, marks))

for name, total in sorted(students.items()):
    print(f"{name:10} {total}")
