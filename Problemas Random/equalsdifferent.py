def solution(x, A):
	x = int(x)
	A = map(int, A.split())
	equalList = equalNumbers(x, A)
	differentList = difNumbers(x, A)
	print 'equals: ', equalList
	print 'differ: ', differentList

	i = 0
	while i < len(A):
		if equalList[i] == differentList[i]:
			return i
		i = i + 1
	return - 1

def equalNumbers(x, A):
	B = []
	i = 0
	repetitions = 0
	while i < len(A):
		B.append(repetitions)
		if A[i] == x:
			repetitions = repetitions + 1
		i = i + 1
	return B

def difNumbers(x, A):
	B = [0] * len(A)
	i = len(A) - 1
	differents = 0
	while i >= 0:
		if A[i] != x:
			differents = differents + 1
		B[i] = differents
		i = i - 1
	return B

print 'result: ', solution(raw_input('Enter int: '), raw_input('Enter int list: '))