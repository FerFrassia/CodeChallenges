from collections import deque

def morgan(a, b):
	stackA = deque()
	stackB = deque()
	fill(stackA, a)
	fill(stackB, b)
	minimalString = ''
	while (len(stackA) > 0 or len(stackB) > 0):
		charToInsert = ''
		if (len(stackA) > 0 and len(stackB) == 0):
			charToInsert = stackA.popleft()
		elif (len(stackA) == 0 and len(stackB) > 0):
			charToInsert = stackB.popleft()
		else:
			if (stackA[0] < stackB[0]):
				charToInsert = stackA.popleft()
			else:
				charToInsert = stackB.popleft()
		minimalString = minimalString + charToInsert
	return minimalString

def fill(myStack, s):
	for char in s:
		myStack.append(char)


print morgan('ABACABA', 'ABACABA')