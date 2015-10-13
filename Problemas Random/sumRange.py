def precalculate(l):
	sumList = []
	partialSum = 0
	i = 0
	while (i < len(l)):
		partialSum += l[i]
		sumList.append(partialSum)
		i += 1
	return sumList

def sumInRange(l, i, j):
	if (i != 0):
		return l[j] - l[i-1]
	else:
		return l[j]

totalSum = precalculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print totalSum
print sumInRange(totalSum, 2, 4)
print sumInRange(totalSum, 0, 9)
