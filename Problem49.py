primes = [2, 3, 5, 7, 11, 13]
def isPrime(n):
    if n in primes:
        return True
    else:
        if n % 2 == 0:
            return False
        
        j = 3
        while j ** 2 <= n:
            if n % j == 0:
                return False
            j += 2
        primes.append(n)
        return True

def checkPermPrime(primes):
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 != p2 and p2 != p3 and p1 != p3:
                    if p1 < p2 and p2 < p3 and p2 - p1 == p3 - p2:
                        print(p1, p2, p3)  

fourPrimes = {}
for i in range(10**3, 10**4):
    if isPrime(i):
        digSortPrime = "".join(sorted(str(i)))
        if digSortPrime in fourPrimes:
            fourPrimes[digSortPrime].append(i)
        else:
            fourPrimes[digSortPrime] = [i]
# print(fourprimes)
for key, value in fourPrimes.items():
    if len(value) >= 3:
        # print(value)
        checkPermPrime(value)

