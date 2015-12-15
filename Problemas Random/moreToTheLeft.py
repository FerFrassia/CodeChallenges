def moreToTheLeft(l, begin, end):
	if begin == end:
		return True
	else:
		middle =  begin + (end-begin)/2 
		leftSum = 0
		rightSum = 0
		i = begin
		while i <= end:
			if i <= middle:
				leftSum += l[i]
			else:
				rightSum += l[i]
			i += 1

		if leftSum < rightSum:
			return False
		else:
			return True and moreToTheLeft(l, begin, middle) and moreToTheLeft(l, middle+1, end)


print moreToTheLeft([8, 4, 7, 6, 5, 1, 3, 2], 0, 7)

