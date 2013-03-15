# http://projecteuler.net/problem=25
# What is the first term in the Fibonacci sequence to contain 1000 digits?
def prob25():
	first = 1
	second = 0
	sum = 0
	term = 0
	while len(str(sum)) < 1000:
		sum = first + second
		first = second
		second = sum
		term += 1
	return term

prob25()
