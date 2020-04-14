input = ['Steve,90,77,67,88', 'Jason,88,76,88', 'Dagny,98,77,60,87', "Henry,88,66,77"]

students = {}

for s in input:
    parts = s.split(",")
    
    # place all marks as numbers int marks list
    marks = []
    for v in parts[1:]:
        marks.append(int(v))

    # Place name as key and list of marks as value
    students[parts[0]] = marks

# print(students)

for name, marks in sorted(students.items()):
    print(f"{name:10} {sum(marks)}")
