f = open("mobiles.txt", "rt")

mobiles = []
for line in f.readlines():
    parts = line.strip().split(',')
    mobiles.extend(parts)

f.close()

for mobile in sorted(mobiles):
    print(mobile)
