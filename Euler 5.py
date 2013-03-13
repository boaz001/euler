# http://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def prob5(n):
  print "finding the smallest positive number that is evenly divisible by all of the numbers from 1 to", n
  number = 1 # start from number 1
  remainder = 1 # is there a remainder
  i = 0
  while remainder == 1:
    while i<n:
      if number%(i+1) == 0:
        remainder = 0
      else:
        remainder = 1
      if remainder == 1:
        number = number + 1
        remainder = 1
        i = 0
      else:
        remainder = 0
        i = i+1
  print "Answer:"
  return number

prob5(20)
