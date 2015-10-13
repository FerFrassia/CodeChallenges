storedValues = {}

def f(n):
	global storedValues
	if (n in storedValues):
		return storedValues[n]
	else:
		if (n == 1):
			storedValues[n] = 0
			return 0
		else:			
			m = 0
			if (n % 2 == 0):
				m = n / 2
			else:
				m = 3*n+1
			
			toStore = 1 + f(m)
			storedValues[n] = toStore
			return toStore

def manyQuerys(l):
	for elem in l:
		print 'f(' + str(elem) + '): ', f(elem)

manyQuerys([1, 2, 3, 5, 6, 7, 8])
print 'stored values: ', storedValues

# 5
# 16
# 8
# 4
# 2
# 1