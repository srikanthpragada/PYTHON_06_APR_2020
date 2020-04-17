# nums = ['10', '20', '25', '60', '88']
# ints = map(int, nums)
# print(sum(ints))

nums = ['A10', 'B20', 'A25', 'C60', 'D88']
ints = map(lambda v: int(v[1:]), nums)
print(sum(ints))
