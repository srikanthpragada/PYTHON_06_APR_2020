st = "How do you do. Hope you are doing great!"
ss = "do"

pos = -1
while True:
    pos = st.find(ss, pos + 1)
    if pos == -1:
        break

    print(pos)
