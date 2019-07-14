import re

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

primes = [x for x in range(10000) if isprime(x)]
squares = [n * n for n in range(10000)]

odds = [2 * n + 1 for n in range(10000)]

for s in squares:
    for p in primes:
        o = p + 2 * s
        if o in odds:
            odds.remove(o)

print(odds)
