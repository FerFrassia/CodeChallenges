import math

def amountOfSquares(a, b):
	currentNumber = a
	while currentNumber <= b and math.sqrt(currentNumber) != int(math.sqrt(currentNumber)):
		currentNumber += 1

	counter = 0
	if currentNumber > b:
		# there are no squares
		return counter
	else:
		# currentNumber is the first square
		currentSqrt = math.sqrt(currentNumber)
		while currentSqrt**2 <= b:
			counter += 1
			currentSqrt += 1

		return counter


print amountOfSquares(17, 24)


# Problem Statement

# Watson gives two integers (A and B) to Sherlock and asks if he can count the number of square integers
#  between A and B (both inclusive).

# Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 
# are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.