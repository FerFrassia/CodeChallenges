def bubbleSort(l):
	print l
	i = 0
	while i < len(l):
		j = i+1
		while j < len(l):
			if l[i] > l[j]:
				l[i], l[j] = l[j], l[i]
			j += 1
		print l
		i += 1

	print l

bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
#bubbleSort([5, 3, 7, 6, 1, 9, 2, 4, 10, 8])