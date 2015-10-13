def nextPalindrome(n):
	li = [int(i) for i in str(n)]
	if (len(li) == 1):
		return n+1
	else:
		i = 0
		j = len(li) -1
		changesMade = False
		while (i < j):
			if (li[i] < li[j]):
				li[j-1] = li[j-1]+1
				li[j] = li[i]
				changesMade = True
			elif (li[i] > li[j]):
				li[j] = li[i]
				changesMade = True
			i += 1
			j -= 1		

		if (not changesMade):
			return nextPalindrome(n+1)
		else:
			return int(''.join(map(str, li)))

inputCases = int(raw_input())
while (inputCases > 0):
	inputN = int(raw_input())
	print nextPalindrome(inputN)
	inputCases -= 1
