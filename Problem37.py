def generatePrimes(upperLimit):
    primes = [2]
    for num in range(3, upperLimit, 2):
        isPrime = True
        for p in primes:
            if num % p == 0:
                isPrime = False
                break
            if p*p > num:
                break
        if isPrime:
            primes.append(num)
    return primes

def isLeftTruncatable(num):
    if num < 11:
        if num in [2, 3, 5, 7]:
            return True
        else:
            return False
    elif num in primes:
        return isLeftTruncatable(int(str(num)[1:]))
    else:
        return False

        
def isRightTruncatable(num):
    if num < 11:
        if num in [2, 3, 5, 7]:
            return True
        else:
            return False
    elif num in primes:
        return isRightTruncatable(int(str(num)[:-1]))
    else:
        return False

def isBiTruncatable(num):
    if num < 10:
        return False
    return isLeftTruncatable(num) and isRightTruncatable(num)

ans = []
primes = generatePrimes(1000000)
print(len(primes))
for p in primes:
    if isBiTruncatable(p):
        ans.append(p)

print(len(ans))
print(ans)
print(sum(ans))