# Very naive solution

odds = [1, 3, 5, 7, 9]
primes = []
a = 10**6
nums = [2] + [i for i in range(3, a, 2)]

# list of odd primes under a million
for i in range(3,int(a**(1/2)), 2):
    nums = list(filter(lambda x: x == i or x % i != 0, nums))

# print(len(nums))

seen = []
count = 0 
for num in nums:
    count += 1
    if count == 1000:
        count = 0
        print(num)
    if num in seen:
        continue
    n = str(num)
    flag = 0
    seen_t = []
    n_t = n
    for digit in n:
        n_t = n_t[1:] + n_t[:1]
        seen_t.append(int("".join(n_t)))
        if int("".join(n_t)) not in nums:
            flag = 1
            continue

    if flag == 0:
        seen += seen_t

print(len(set(seen)))

