sum = 1
pos = 1
for i in xrange(2, 1001 +1, 2):
  for j in range(4):
      pos += i
      sum += pos
print sum
