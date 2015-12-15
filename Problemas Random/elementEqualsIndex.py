def elementEqualsIndex(l, begin, end):
	if begin == end:
		if l[begin] == begin:
			return begin
		else:
			return None
	else:
		middle = begin + (end-begin)/2

		if l[middle] == middle:
			return middle
		else:
			if l[middle] < middle:
				return elementEqualsIndex(l, middle+1, end)
			else:
				return elementEqualsIndex(l, begin, middle)

myList = [0, -4, -1, 2, 4, 7]
print elementEqualsIndex(myList, 1, 5)