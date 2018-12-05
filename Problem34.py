# The number can be at most 6 digits
# This would be 10^6 combinations, which isn't too terrible
# To improve this, we can either iterate through lengths seperately, or impose constraints before doing all the computation
#
# If the largest digit in a number a with length l is k with length n, k! < a <= k!*l, n <= l <= n+1.
# I will use k! < a <= k!*(n+1) because I feel like it

factorials = [1]
while(len(factorials) < 10):
    factorials.append(factorials[-1]*len(factorials))
f_len = [len(str(f)) for f in factorials]

total = 0
for i in range(3, factorials[-1]*(f_len[-1]+1)):
    m = list(map(int, sorted(str(i))))

    if factorials[m[-1]] > i or i > factorials[m[-1]] * len(m):
        continue
    s = sum([factorials[k] for k in m])

    if s == i:
        print(i)
        total += s
print(total)
