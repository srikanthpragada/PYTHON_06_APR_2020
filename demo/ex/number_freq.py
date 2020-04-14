input = [40, 50, 66, 55, 44, 40, 50, 66, 30]

freq = {}

for n in input:
    if n in freq:
        freq[n] += 1  # increment count
    else:
        freq[n] = 1

print(sorted(freq.items()))
