# http://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n):
    d = 2
    while n > 1 and d < n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def prob7():
    prime_count = 0
    number = 1
    while prime_count != 10001:
        number = number + 1
        if is_prime(number):
            prime_count += 1
    print number

prob7()
