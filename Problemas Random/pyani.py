#input: list of ints, the first one is the number of pyanis, the others are the pyanis
#output: the pyani that does not repeat itself


def pyaniTuples(l):
	l = map(int, l.split())
	repeatedPyanis = [None] * (((len(l) - 2) / 2)+1)
	i = 1
	j = 0
	while (i < len(l)):
		tupPyaniFalse = (l[i], False)
		if (tupPyaniFalse in repeatedPyanis):
			tupPyaniTrue = (l[i], True)
			repeatedPyanis[repeatedPyanis.index(tupPyaniFalse)] = tupPyaniTrue
		else:
			repeatedPyanis[j] = tupPyaniFalse
			j = j+1
		i = i+1

	j = 0
	while (j < len(repeatedPyanis)):
		if (repeatedPyanis[j][1] == False):
			return repeatedPyanis[j][0]
		else:
			j = j+1

def pyaniSort(l):
	l = map(int, l.split())
	del l[0]
	l.sort()
	i = 0
	if (len(l) == 1 or l[i] != l[i+1]):
		return l[i]		
	while(i < len(l) - 2):
		if (l[i] != l[i+1] and l[i+1] != l[i+2]):
			return l[i+1]
		i = i+1
	if (l[i] != l[i+1]):
		return l[i+1]

def pyaniNum(a, b):
	xor(bin(a), bin(b))


# inputPyanis = raw_input('Enter Pyani list (example: 3 1 8 1): ')
# l = map(int, l.split())
# print 'pyaniTuples: ', pyaniTuples(inputPyanis)
# print 'pyaniSort: ', pyaniSort(inputPyanis)
# print 'pyaniNum: ', pyaniNum(inputPyanis)
print pyaniNum(1, 2)

	