# def biggerString(l):
# 	i = len(l)-1
# 	while (i > 0 and l[i-1] >= l[i]):
# 		i -= 1

# 	if (i == 0):
# 		return 'not possible'

# 	i -= 1
# 	j = len(l)-1
# 	while (j > i and l[j] <= l[i]):
# 		j -= 1

# 	bufferValue = l[i]
# 	l[i] = l[j]
# 	l[j] = bufferValue

# 	i += 1
# 	l = l[:i] + l[i:][::-1]

# 	return l

# print biggerString([0, 1, 2, 5, 3, 3, 0]) 



def biggernNum(l1, l2, i):
	if (i == len(l1)-1):
		if (l1[i] >= l2[i]):
			return [-1]
		else:
			return [l2[i]]
	else:
		if (l1[i] >= l2[i]):
			indexEqual = -1
			indexGreater = -1
			if (l1[i] == l2[i]):
				indexEqual = i
			j = i+1
			while (j < len(l2)):
				if (l2[j] > l1[i]):
					if (indexGreater == -1):
						indexGreater = j
					else:
						maxVal = min(l2[j], l2[indexGreater])
						if (maxVal == l2[j]):
							indexGreater = j
				if (indexEqual == -1 and l2[j] == l1[i]):
					indexEqual = j
				j += 1
			if (indexEqual == -1 and indexGreater == -1):
				return [-1]
			elif (indexEqual == -1 and indexGreater != -1):
				bufferValue = l2[i]
				l2[i] = l2[indexGreater]
				l2[indexGreater] = bufferValue
				i += 1
				return l2[:i] + sorted(l2[i:])
			elif (indexEqual != -1 and indexGreater == -1):
				bufferValue = l2[i]
				l2[i] = l2[indexEqual]
				l2[indexEqual] = bufferValue
				i += 1
				equalPut = biggernNum(l1, l2, i)
				if ()









