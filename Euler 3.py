# http://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(n):
    largest = None
    d = 2
    while n > 1:
        while n % d == 0:
            largest = d
            n = n / d
        d = d + 1
    return largest

def prob3():
    number = 600851475143
    factor = largest_prime_factor(number)
    if factor == None:
        print number, "Does not have a prime factor"
    else:
        print factor

prob3()
