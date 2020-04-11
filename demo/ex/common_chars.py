# Print common chars between two strings

s1 = "ABCXYZPQRAB"
s2 = "DEFAHBXA"

common = []

for c in s2:
    if c in s1:
        if c not in common:
            common.append(c)

print(common)
