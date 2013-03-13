# http://projecteuler.net/problem=16
# What is the sum of the digits of 2**1000
def prob16():
  num = 2**1000
  string = str(num)
  i = -len(string)
  sumstr = 0
  while i < 0:
    sumstr += int(string[i])
    i += 1
  return sumstr
