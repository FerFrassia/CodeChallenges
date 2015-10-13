def closest_number(a, b):
	strA = map(int, str(a))
	strB = sorted(map(int, str(b)))

	minimalGreater = []
	i = 0
	while (i < len(strA)):
		selectedInt = binSearch(strB, i, strA[i])
		minimalGreater.append(selectedInt)
		if (selectedInt > strA[i]):
			minimalGreater = minimalGreater + strB[i+1:]
			s = ''.join(map(str, minimalGreater))
			return int(s)
		else:
			i += 1

	print 'about to execute'
	s = ''.join(map(str, minimalGreater))
	return int(s)


def binSearch(l, i, element):
	lower = i
	upper = len(l) - 1
	while (lower < upper - 1):
		if ((upper - lower) % 2 == 0):
			currentIndex = (upper - lower) / 2
		else:
			currentIndex = ((upper - lower) / 2) + 1
		if (l[currentIndex] == element):
			bufferElement = l[0]
			l[0] = l[currentIndex]
			l[currentIndex] = bufferElement
			return l[0]
		else:
			if (l[currentIndex] < element):
				lower = currentIndex
			else:
				upper = currentIndex

	if (l[lower] == element):
		currentIndex = lower
	else:
		currentIndex = upper
	
	bufferElement = l[0]
	l[0] = l[currentIndex]
	l[currentIndex] = bufferElement
	return l[0]


print closest_number(1237, 2143)
