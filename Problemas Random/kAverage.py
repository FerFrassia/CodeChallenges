from __future__ import division
from collections import deque

k = 4
kNumbers = deque()
average = 0

def averageKNumbers(n):
	global kNumbers
	global average

	if (len(kNumbers) < k):
		bla = len(kNumbers)
		average = ((average * len(kNumbers)) + n) / (len(kNumbers)+1)
		kNumbers.append(n)
	else:
		average = ((average * len(kNumbers)) - kNumbers[0] + n) / len(kNumbers)
		kNumbers.popleft()
		kNumbers.append(n)
	return average

averageKNumbers(5)
averageKNumbers(10)
averageKNumbers(12)
averageKNumbers(8)
averageKNumbers(4)
averageKNumbers(6)
print averageKNumbers(-1)