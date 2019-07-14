pentagonals = [ x * (3 * x - 1)//2 for x in range(1,10000)]

for i, p1 in enumerate(pentagonals):
    for p2 in pentagonals[:i]:
        if p1 + p2 in pentagonals and p1 - p2 in pentagonals:
            print(p1-p2)

# print(pentagonals)