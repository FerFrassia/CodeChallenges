def orderStrings(stringsList):
	i = 0
	while i < len(stringsList):
		j = i
		minStringIndex = i
		while j < len(stringsList):
			if orderTwoStrings(list(stringsList[j]), list(stringsList[minStringIndex])):
		 		minStringIndex = j
		 	j = j + 1
		IVal = stringsList[i]
		minStringVal = stringsList[minStringIndex]
		stringsList[i] = minStringVal
		stringsList[minStringIndex] = IVal
		i = i + 1

	return stringsList

def orderTwoStrings(a, b):
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			return True
		elif a[i] > b[j]:
			return False
		i = i + 1
		j = j + 1

	if i == len(a) and j != len(b):
		return True
	elif i != len(a) and j == len(b):
		return False
	else:
		return True


def printList(l):
	for index, val in enumerate(l):
		print val
		


#print orderTwoStrings(list(raw_input('first list of chars: ')), list(raw_input('second list of chars: ')))
printList(orderStrings(raw_input('enter list of strings: ').split(' ')))

#it's just a selection sort


