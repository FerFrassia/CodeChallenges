def biggestJoint(l):
	partialBiggest = []
	startIndex = 0
	i = 0
	while (i < len(l)-1):
		if (l[i] + 1 != l[i+1]):
			if (i-startIndex+1 > len(partialBiggest)):
				partialBiggest = l[startIndex:i+1]
			startIndex = i+1
		elif (i == len(l)-2):
			if (i-startIndex+2 > len(partialBiggest)):
				partialBiggest = l[startIndex:]

		i += 1

	return partialBiggest

print biggestJoint([1, 2, 4, 5, 6, 8, 10, 11, 12, 13])