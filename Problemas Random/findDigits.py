def findDigits(n):
	counter = 0
	startupNumber = n
	while n != 0:
		currentDigit = n % 10
		if currentDigit != 0 and startupNumber % currentDigit == 0:
			counter += 1
		n = n/10

	return counter

print findDigits(114108089)







# Problem Statement

# Given an integer, N, traverse its digits (d1,d2,...,dn) and determine 
# how many digits evenly divide N (i.e.: count the number of times N divided by each digit di has a remainder of 0). 
# Print the number of evenly divisible digits.

# Note: Each digit is considered to be unique, 
# so each occurrence of the same evenly divisible digit should be counted (i.e.: for N=111, the answer is 3).