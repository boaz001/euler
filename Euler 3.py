# http://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?
# Project Euler problem 3
def largep(n, d):
	if n%d == 0:
		largep(n-1, d-1)
	else:
		return 1

def run(n):
	done = 0
	d = n-1
	while done != 1:
		if largep(n, d) == 1:
			d -= 1
			done = largep(n, d)
		elif largep(n, d) == -1:
			n -= 1
			d = n-1
			done = largep(n, d)
	return n

#from the interwebs, makes my mac hang
plist = [2]

def primes(min, max):
	if 2 >= min: yield 2
	for i in range(3, max, 2):
		for p in plist:
			if i%p == 0 or p*p > i: break
		if i%p:
			plist.append(i)
			if i >= min: yield i

def factors(number):
	for prime in primes(2, number):
		if number % prime == 0:
			number /= prime
			yield prime
		if number == 1:
			break

print max(factors(317584931803))