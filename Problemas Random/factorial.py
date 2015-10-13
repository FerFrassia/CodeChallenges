factDict = {}
def factorial(n):
	global factDict
	if (n in factDict):
		print 'precalculated ' + str(n) + ': ' + str(factDict[n])
		return factDict[n]
	else:
		print 'calculating: ' + str(n)
		if (n == 1):
			factDict[n] = 1
			return 1
		else:
			toStore = n * factorial(n-1)
			factDict[n] = toStore
			return toStore

factorial(10)
print factDict

print 'factorial 6: ' + str(factorial(6)) + '\n'
print 'factorial 10: ' + str(factorial(10)) + '\n'
print 'factorial 11: ' + str(factorial(11)) + '\n'
print 'factorial 11: ' + str(factorial(11))