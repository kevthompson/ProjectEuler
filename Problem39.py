p = 1000
solutions = [0 for _ in range(p+1)]
for a in range(1, p):
    for b in range(a, p):
        c = (a**2 + b**2)**(1/2)
        if b > c or a > c or a + b + c > p:
            break
        if c % 1 == 0:
            if a + b + c == p:
                print(a, b, c)
            solutions[int(a + b + c)] += 1

print(max(solutions), solutions.index(max(solutions)), solutions)