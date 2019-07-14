r_primes = [1, 2, 3, 5, 7, 11, 13, 17]
r_primes.reverse()

def isPandigital(n):
    n_str = sorted(str(n))
    for i, char in enumerate(n_str):
        if i == len(n_str)-1:
            return True
        elif char == n_str[i+1]:
            return False
    return True

def overlaps(n, m_str):
    n_str = str(n)
    if n < 100:
        n_str = '0' + n_str
    if n_str[1:] == m_str[:2]:
        return n_str[0] + m_str
    else:
        return None

solutions = []
for i, prime in enumerate(r_primes):
    new_solutions = []
    divisor = 1
    while prime * divisor < 1000:
        dividend = prime * divisor
        if isPandigital(dividend):
            if i > 0:
                for n in solutions:
                    ol = overlaps(dividend, n)
                    if ol is not None and isPandigital(ol):
                       new_solutions.append(ol)
            else:
                d_str = str(dividend)
                if dividend < 100:
                    d_str = '0' + d_str
                new_solutions.append(d_str)

        divisor += 1
    solutions = new_solutions
print(solutions)
s_int = list(map(int, solutions))
print(sum(s_int))    


