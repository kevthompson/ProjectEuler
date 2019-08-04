i = 1
sol = False
while not sol:
    i_str = str(i)

    # for j in [2]:
    for j in [2, 3, 4, 5, 6]:
        if sorted(i_str) != sorted(str(j * i)):
            break    
    else: 
        sol = True
    
    if sol:
        for j in [1, 2, 3, 4, 5, 6]:
            print(j, i*j)
    
    i += 1
