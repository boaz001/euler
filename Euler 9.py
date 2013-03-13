# http://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def prob9():
  solution = 0
  a = 0
  b = 0
  c = 0
  while solution == 0:
    for a in range(500):
      for b in range(500):
        for c in range(500):
          #print a, b, c
          if (a+b+c == 1000) & (a**2+b**2 == c**2) & (a<b) & (b<c) & (a != 0 and b != 0 and c != 0):
            solution = 1
            print "solution found! a=", a, "b=", b, "c=", c
            return a*b*c
          else:
            solution = 0

prob9()
