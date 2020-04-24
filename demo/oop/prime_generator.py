def primes(start, end):
    print("Primes")
    for n in range(start, end + 1):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n


pn = primes(50, 100)

print(next(pn))
print(next(pn))
