# http://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers.
def ispalindrome(n):
  nstring = str(n)
  length = len(nstring)
  if length == 1:
    return 1
  elif length%2 == 0:
    # length is even
    for i in range(length/2):
      cont = 0
      if nstring[i:i+1] == nstring[length-i-1:length-i]:
        cont = 1
      if cont == 0:
        return 0
    return 1
  else:
    # length is uneven (don't have to check the digit in the middle)
    for i in range((length-1)/2):
      cont = 0
      if nstring[i:i+1] == nstring[length-i-1:length-i]:
        cont = 1
      if cont == 0:
        return 0
    return 1

def prob4():
  a = 1
  b = 1
  maxpal = 0
  for a in range(1000):
    for b in range(1000):
      prod = a*b
      if (ispalindrome(prod)):
        if prod > maxpal:
          maxpal = prod
  return maxpal

prob4()
