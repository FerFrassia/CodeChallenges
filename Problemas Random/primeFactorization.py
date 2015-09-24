primesList = []

def primeFactorization(n, i):
	if (n == 1 and i == 2):
		primesList.append((n, 1))
	elif (n == 1):
		return
	else:
		if (n % i == 0):
			if (len(primesList) == 0):
				primesList.append((i, 1))
			else:
				if (primesList[-1][0] == i):
					primesList[-1] = (primesList[-1][0], primesList[-1][1] + 1)
				else:
					primesList.append((i, 1))
			n = n / i
		else:
			i += 1
		primeFactorization(n, i)


def sngint(n):
	primeFactorization(n, 2)
	l = primesList
	if (len(l) == 1):
		if (len(str(l[0][0])) < 2):
			return l[0][0]
		else:
			return -1
	else:
		i = 0
		sngIntList = []
		while (i < len(l)):
			sngIntList.append(str(pow(l[i][0],l[i][1])))
			i += 1
		return ''.join(sngIntList)


def sngForList(l):
	sngIntToReturn = []
	for elem in l:
		primesList = []
		sngIntToReturn.append(sngint(elem))
	return sngIntToReturn


print sngForList([24, 5, 11])


