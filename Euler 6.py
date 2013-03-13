# http://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Project Euler problem 6
import math
def prob6(n):
	i = 0
	sum_sq = 0
	sq_sum = 0
	sum = 0
	diff = 0
	while i<=n:
		sq_sum += i**2
		sum += i
		sum_sq = sum**2
		diff = sq_sum - sum_sq
		i += 1
	return math.fabs(diff)

prob6(100)
