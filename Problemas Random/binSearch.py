def binSearch(l, lower, upper, n):
	if (lower == upper):
		return lower
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


print binSearch([1, 3, 5, 6, 7, 9], 0, 5, 6)