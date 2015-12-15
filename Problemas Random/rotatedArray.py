def kRotated(l):
	i = 0
	while (i < len(l)-1):
		if (l[i] > l[i+1]):
			break
		i += 1

	i += 1
	if (i == len(l)):
		i = 0
	return i

print kRotated([4, 5, 1, 2, 3])
