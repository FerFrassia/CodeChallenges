def checkPermutations(a, b):
	if (len(a) != len(b)):
		return False

	i = 0
	while (i < len(a)):
		if (b.find(a[i]) == -1 or a.find(b[i]) == -1):
			return False
		i = i + 1

	return True


#takes two strings, checks if one is a permutation of the other one
def bruteForcePermutated(a, b):
	permutationsList = permutations(list(a))
	if (b in permutationsList):
		return True
	else:
		return False


#takes a list of chars
#returns list of strings
def permutations(a):
	if len(a) < 2:
		return a
	else:
		choppedChar = a[-1]
		del a[-1]
		aux = permutations(a)
		res = []
		for index, value in enumerate(aux):

			permutatedValueList = addCharEverywhere(list(value), choppedChar)
			for index, value in enumerate(permutatedValueList):
				res.append(value)
		return res

#a is list of chars, c is char
#it returns list of strings, with c meddling in all positions
def addCharEverywhere(a, c):
	res = []
	i = 0
	while (i < len(a)):
		copyA = a[:]
		copyA.insert(i, c);
		copyA = ''.join(copyA)
		res.append(copyA)
		i = i + 1

	#add c to last position
	copyA = a[:]
	copyA.append(c);
	copyA = ''.join(copyA)
	res.append(copyA)

	return res

inputString1 = raw_input('Enter string 1: ')
inputString2 = raw_input('Enter string 2: ')

#print 'They are permutations: ', bruteForcePermutated(inputString1, inputString2)
print 'They are permutations: ', checkPermutations(inputString1, inputString2)
#checkPermutations(inputString1, inputString2)
