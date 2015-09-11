def solution(A):
	A = map(int, A.split())
	i = len(A) - 1
	B = []
	carry = 0
	print 'A: ', A
	while i >= 0:
		if A[i] == 1:
			if carry == 1:
				B.insert(0, 0)
				carry = 1
			else:
				B.insert(0, 1)
				carry = 1
		else:
			if carry == 1:
				B.insert(0, 1)
				carry = 1
			else:
				B.insert(0, 0)
		i = i - 1
	return shortenByZeros(B)

def shortenByZeros(A):
	i = 0
	while i < len(A) and A[i] == 0:
		A.pop(0)
		i = i + 1
	return A

print '-Number: ', solution(raw_input('Enter int list: '))