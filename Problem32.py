import copy
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Only 2 digit * 3 digit  or 1 digit * 4 digit will work
solutions = []
for i in range(9):
    for j in range(8):
        orig = copy.deepcopy(digits)
        dig1 = str(digits.pop(i))
        dig2 = str(digits.pop(j))
        num1 = int(dig1 + dig2)

        flag = 0
        for k in range(7):
            for l in range(6):
                for m in range(5):
                    orig2 = copy.deepcopy(digits)
                    dig3 = str(digits.pop(k))
                    dig4 = str(digits.pop(l))
                    dig5 = str(digits.pop(m))
                    num2 = int(dig3+dig4+dig5)
                    prod = num1 * num2
                        
                    s = sorted(str(prod) + str(num1) + str(num2))
                    if s == [str(i) for i in range(1, 10)] and prod not in solutions:
                        solutions.append(prod)
                    digits = orig2
                        
                    if flag == 1:
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
        # print(digits)
        digits = orig

for i in range(9):
    orig = copy.deepcopy(digits)
    dig1 = str(digits.pop(i))
    num1 = int(dig1)

    flag = 0
    for j in range(8):
        for k in range(7):
            for l in range(6):
                for m in range(5):
                    orig2 = copy.deepcopy(digits)
                    dig2 = str(digits.pop(j))
                    dig3 = str(digits.pop(k))
                    dig4 = str(digits.pop(l))
                    dig5 = str(digits.pop(m))
                    num2 = int(dig2+dig3+dig4+dig5)
                    prod = num1 * num2
                    s = sorted(str(prod) + str(num1) + str(num2))
                    if s == [str(i) for i in range(1, 10)] and prod not in solutions:
                        solutions.append(prod)
                    digits = orig2

                    if flag == 1:
                        break    
                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
    # print(digits)
    digits = orig


print (sum(solutions))