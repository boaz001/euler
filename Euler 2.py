# http://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Project Euler problem 2
def prob2():
	first = 1
	second = 1
	sum = 0
	evensum = 0
	while sum <= 4000000:
		sum = first + second
		first = second
		second = sum
		if sum%2 == 0:
			evensum += sum
	return evensum

prob2()
