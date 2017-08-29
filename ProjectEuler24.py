import numpy
import math
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sol = []
target = 999999
counter = 10
for i in arr2:
	temp = math.floor(target / math.factorial(counter-1))
	target -= temp*math.factorial(counter-1)
	sol.append(arr[temp])
	del arr[temp]
	print(arr, sol, temp)
	counter -= 1

