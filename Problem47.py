import re

def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

primes = [x for x in range(10000) if isprime(x)]

def primeFactors(n):
    factors = []
    for i in primes:
        if n % i == 0:
            factors.append(i)

        while n % i == 0:
            n //= i
        if n == 1:
            return factors

    return factors

n = 2
c = 0
while c < 4:
    f = primeFactors(n)
    if len(f) == 4:
        c += 1
        if c == 4:
            print(n - 3)
            break
    else:
        c = 0
    n += 1
