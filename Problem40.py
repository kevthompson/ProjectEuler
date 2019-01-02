length = 6 # we go up to 10 ** length integers
stringified = "".join(list(map(str, range(10**length + 1))))
product = 1
for i in range(length+1):
    product *= int(stringified[10**i])
    print(product)