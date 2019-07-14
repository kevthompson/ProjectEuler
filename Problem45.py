triangles = [n * (n + 1) // 2 for n in range(1, 100000)]
pentagonals = [n * (3 * n - 1) // 2 for n in range(1, 50000)]
hexagonals = [n * (2 * n - 1) for n in range(1, 50000)]

for t in triangles:
    if t in pentagonals:
        print (t)
        if t in hexagonals:
            print("!!!!!")