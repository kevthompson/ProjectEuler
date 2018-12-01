coins = [1, 2, 5, 10, 20, 50, 100, 200]
arrangements = [1]*(coins[-1]+1)

for c in coins:
    if c == 1:
        continue
    for n, a in enumerate(arrangements):
        if c <= n:
            # print(c, n, arrangements[n], arrangements[n-c])   
            arrangements[n] += arrangements[n-c]


# print(arrangements)
print([arrangements[i] for i in coins])