def solution(A):
	A = map(int, A.split())
	x = 0
	y = 0
	i = 0
	while i < len(A):
		if i == 0:
			y = y + A[i]
		elif i == 1:
			x = x - A[i]
		elif i == 2:
			y = y - A[i]
		elif i == 3 or i == 4:
			if A[i-1] <= A[i-3] and A[i] >= A[i-2]:
				return i
			else:
				if i == 3:
					x = x + A[i]
				else:
					y = y + A[i]
		else:
			if (A[i-1] <= A[i-3] and A[i] >= A[i-2]) or (A[i-1] - A[i-3] <= A[i-5] and A[i] >= A[i-2] - A[i-4]):
				return i
			else:
				if i%4 == 0:
					y = y + A[i]
				elif i%4 == 1:
					x = x - A[i]
				elif i%4 == 2:
					y = y - A[i]
				else:
					x = x + A[i]
		i = i + 1
	return -1


print 'Movements: ', solution(raw_input('Enter int list: '))
				
