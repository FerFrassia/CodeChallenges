def binSearch(l, lower, upper, n):
	if (lower == upper):
		if (lower == len(l)-1):
			return lower
		else:
			return lower-1
	else:
		middle = (upper-lower)/2
		middle += lower
		if l[middle] == n:
			return middle
		else:
			if (l[middle] < n):
				return binSearch(l, middle+1, upper, n)
			else:
				return binSearch(l, lower, middle, n)

def amountOfPairsThatSumX(l, x):
	l = sorted(l)
	i = binSearch(l, 0, len(l)-1, x)
	amountOfPairs = 0
	while i >= 0:
		restToX = x-l[i]
		j = binSearch(l, 0, i, restToX)
		amountOfPairs += j+1
		i -= 1
	return amountOfPairs

def bruteForce(l, x):
	pairs = []
	i = 0
	while i < len(l):
		j = i+1
		while j < len(l):
			if l[i] + l[j] <= x:
				pairs.append((l[i], l[j]))
			j += 1
		i += 1
	return pairs

print 'smart: ' + str(amountOfPairsThatSumX([2, 4, 6, 5, 9, 7, 8], 10))
print 'brute: ' + str(bruteForce([2, 4, 6, 5, 9, 7, 8], 10))
