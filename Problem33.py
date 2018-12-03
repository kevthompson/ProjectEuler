solutions = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i/j >= 1:
                continue
            elif (10*i+k)/(10*j+k) == i/j or (10*i+k)/(10*k+j) == i/j:
                solutions.append((i, j))

den = 1
for sol in solutions:
    den *= sol[1]

for sol in solutions:
    if den % sol[0] == 0:
        den /= sol[0]



print(solutions, den)