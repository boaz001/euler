# Project Euler problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def prob1(n):
  i = 0
  sum = 0
  additosum = 0
  while i<n:
    if i%3 == 0:
      additosum = 1
    if i%5 == 0:
      additosum = 1
    if additosum == 1:
      sum += i
      additosum = 0
    i = i + 1
  return sum

prob1(1000)
