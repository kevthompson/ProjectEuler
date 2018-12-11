def isPalindrome(string):
    if len(string) == 1:
        return True
    midpoint = (len(string)+1)//2
    # print(string[:midpoint], string[:midpoint-(len(string)%2)-1:-1])
    return string[:midpoint] == string[:midpoint-(len(string) % 2)-1:-1]

s = 0
for i in range(10**6):
    if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:]):
        print(i, str(bin(i)))
        s += i

print(s)