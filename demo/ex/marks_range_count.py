input = [60, 53, 66, 55, 70, 80, 90, 66, 83, 76]

freq = {'51-60': 0, '61-70': 0, '71-80': 0, '81-90': 0, '91-100': 0, }

for n in input:
    if n <= 60:
        freq['51-60'] += 1
    elif n <= 70:
        freq['61-70'] += 1
    elif n <= 80:
        freq['71-80'] += 1
    elif n <= 90:
        freq['81-90'] += 1
    else:
        freq['91-100'] += 1

print(freq.items())
