# Print common chars between two strings

s1 = "ABCXYZPQRAB"
s2 = "DEFAHBXA"

for c in set(s2):
    if c in s1:
       print(c)


