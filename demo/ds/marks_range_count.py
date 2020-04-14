input = [82, 78, 55, 57, 67, 88, 73, 60, 77, 95]

ranges = []
counts = []
start = 51
while start < 100:
    ranges.append(f"{start} - {start + 9}")
    counts.append(0)
    start += 10

for n in input:
    pos = ((n - 1) // 10) - 5
    counts[pos] += 1

for r, c in zip(ranges, counts):
    print(f"{r:10} - {c}")
