# http://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import collections
def prime():
  below = 16
  numbers = {}
  i = 2
  while (i>1 and i<below):
    numbers[i] = True # by default all are prime
    i = i+1
  i = 2
  print numbers
  primes = []

