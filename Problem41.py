# Generate a list of pandigital primes with 'length' digits
def panPrimes(length):
    p = range(10**(length-1)+1, 10**length, 2)
    for i in range(3, int(10**(length/2)), 2):
        p = list(filter(lambda x: isPandigital(x) and (x == i or x % i != 0), p))
        # if (i - 1) % 10**(length-2) == 0:
        print(i)
    return p

def isPandigital(num):
    return sorted(str(num)) == list(map(str, range(1, len(str(num)) + 1)))

pandigitalPrimes = panPrimes(7)
print(pandigitalPrimes)
print(pandigitalPrimes[-1])