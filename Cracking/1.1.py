def allUniques(s):
	s = list(s)
	if (len(s) > 1):
		firstChar = s[0]
		i = 1
		while (i < len(s)):
			if (s[i] != firstChar):
				return False
			i = i + 1
	return True

def allUniques2(s):
	firstChar = s[0]
	uniqueS = firstChar * len(s)
	return uniqueS == s


inputString = raw_input('Insert string: ')
print 'allUniques: ', allUniques(inputString)
print 'allUniques2: ', allUniques2(inputString)