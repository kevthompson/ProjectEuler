def prime_gen(n):
    primes = [2]
    nextPrime = 3

    while nextPrime < n:
        isPrime = True
        i = 0
        squareRoot = int(nextPrime ** .5)

        while primes[i] <= squareRoot:
            if nextPrime % primes[i] == 0:
                isPrime = False
            i += 1

        if isPrime:
            primes.append(nextPrime)

        nextPrime += 2
    return primes

primes = prime_gen(1000000)

for l in range(40, 5000):
    for i in range(len(primes) - l):
        s = sum(primes[i:i+l])
        if s >= 1000000:
            # print (l)
            break
        elif s in primes:
            print(l, s)
            break
