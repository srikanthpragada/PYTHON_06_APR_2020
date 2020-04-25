def contains_digit(s):
    for c in s:
        if c.isdigit():
            return True
    else:
        return False

print(contains_digit("abc123"))