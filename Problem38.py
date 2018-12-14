def numDigits(num):
    return len(str(num))

def isPandigital(num):
    return "".join(sorted(str(num))) == "123456789"

def isPandigitalMultiple(num):
    concatNum = pandigitalMultiple(num)

    return numDigits(concatNum) == 9 and isPandigital(concatNum)

def pandigitalMultiple(num):
    concatNum = num
    multiplier = 2
    while numDigits(concatNum) < 9:
        nextNum = num * multiplier
        concatNum = 10 ** numDigits(nextNum) * concatNum + nextNum
        multiplier += 1
    return concatNum

for i in range(190, 10000):
    if isPandigitalMultiple(i):
        print(i, pandigitalMultiple(i))