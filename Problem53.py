total = 0
for n in range(1, 101):
    for r in range(0, n+1):
        nCr = 1
        for i in range(n-r+1, n+1):
            nCr *= i
        for i in range(1, r+1):
            nCr /= i

        if nCr > 10**6:
            # print(n, r, 2*(r-1), n - 2 * (r-1) - 1)
            total += n - 2 * (r-1) - 1
            break

print(total)