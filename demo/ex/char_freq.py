# Print how many times each letter is present
st = "This is awesome. That is also great".upper()

for n in range(65, 91):
    ch = chr(n)
    print(f"{ch} - {st.count(ch)}")
