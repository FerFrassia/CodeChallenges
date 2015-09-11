def permutations(A):
	if (len(A) == 0):
		return []
	elif (len(A) == 1):
		return A
	else:
		choppedChar = A[len(A)-1]
		del A[-1]
		aux = permutations(A)
		returnable = []
		for index, value in enumerate(aux):
			valueList = list(value)
			#print valueList
			i = 0
			while (i < len(valueList)):
				# print 'valuelist in cycle: ', valueList
				copyValueList = valueList[:]
				copyValueList.insert(i, choppedChar)
				copyValueList = ''.join(copyValueList)
				#print 'copyValueList: ', copyValueList
				returnable.append(copyValueList)
				i = i + 1
			copyValueList = valueList[:]
			copyValueList.append(choppedChar)
			copyValueList = ''.join(copyValueList)
			returnable.append(copyValueList)
		return returnable


A = raw_input('Enter int list: ').split()
print 'permutations: ', permutations(A)
