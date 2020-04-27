import re

f = open("mobiles.txt", "rt")
p = re.compile(r"\d{10}")

mobiles = set()

for line in f:
    matches = p.findall(line)
    for m in matches:
        if len(m) == 10:
            mobiles.add(m)

f.close()

for mobile in sorted(mobiles):
    print(mobile)
