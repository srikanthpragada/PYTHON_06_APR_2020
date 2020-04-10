# Print how many upper, lower and other char are present
st = "This is awesome. That is also great"

upper = lower = other = 0
for ch in st:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        other += 1

print(f"Upper : {upper}, Lower : {lower} , Others : {other}")
