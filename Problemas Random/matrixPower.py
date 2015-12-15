def matrixPower(a, begin, end):
	if begin == end:
		return pot(a, begin)
	else:
		middle = begin + (end-begin)/2

		return matrixPower(a, begin, middle) + matrixPower(a, middle+1, end)


print matrixPower(a, 1, n)