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

def count_duplicates(arr):
    cur = arr[0]
    counts = [0]
    for n in arr:
        if cur != n:
            cur = n
            counts.append(0)    
        counts[-1] += 1
    return counts


for n in range(4, 8):
    print(n)
    primes1 = list(map(str, prime_gen(10**(n-1))))
    primes2 = list(map(str, prime_gen(10**(n+0))))[len(primes1):]
    for i in range(n):
        # trimmed = sorted([p[:i] + p[i+1:] for p in primes2])
        for j in range(i):
            # trimmed = sorted([p[:j] + p[j+1:i] + p[i+1:] for p in primes2 if p[j] == p[i]])    
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        trimmed = sorted([p[:m] + p[m+1:l] + p[l+1:k] + p[k+1:j] + p[j+1:i] + p[i+1:] for p in primes2 if p[l] == p[k] == p[j] == p[i]])
                        if len(trimmed) == 0:
                            continue
                        cur = trimmed[0]
                        count = 0
                        ans = 0
                        for idx, n in enumerate(trimmed):
                            if cur != n:
                                if count == 8:
                                    print(i, j, k, l, m, ans)
                                ans = n
                                cur = n
                                count = 0   
                            count += 1
                      
n = 6
primes1 = list(map(str, prime_gen(10**(n-1))))
primes2 = list(map(str, prime_gen(10**(n+0))))[len(primes1):]
for p in primes2:
    if p[5] == p[3] == p[4] == p[1] == p[0]:
        print(p)
