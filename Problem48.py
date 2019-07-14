s = 0
mod = 10 ** 10
for i in range(1, 1001):
    s += i ** i 
s %= mod
print(s)