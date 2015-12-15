def insertionSort(l):
	i = 0
	while i < len(l):
		j = i
		x = l[i]
		while j > 0 and l[j-1] > x:
			l[j] = l[j-1]
			j -= 1
		l[j] = x
		print l
		i += 1

	print l

#insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
insertionSort([5, 3, 7, 6, 1, 9, 2, 4, 10, 8, 0])