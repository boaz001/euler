# http://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!
def prob20(n):
  fac = n
  while n > 1:
    fac *= n-1
    n -= 1
  facstr = str(fac)
  facstrsum = 0
  for i in range(len(facstr)):
    facstrsum += int(facstr[i])
  return facstrsum

prob20(100)
