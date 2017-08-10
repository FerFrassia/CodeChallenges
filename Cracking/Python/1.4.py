#takes a string
#returns string, with %20 instead of spaces
def separateBy20UsingInsert(s):
	s = list(s)
	i = 0
	while (i < len(s)):
		if (s[i] == ' '):
			s[i] = '%'
			s.insert(i+1, '2')
			s.insert(i+2, '0')
		i = i + 1
	s = ''.join(s)
	return s

def separateBy20UsingSwap(s):
	if (s != ''):
		s = joinSpaces(list(s))
		i = 0 
		while (i < len(s)):
			if (s[i] == ' '):
				s[i] = '%'
				s[i+1] = '2'
				s[i+2] = '0'
			i = i + 1
		s = ''.join(s)
	return s

#takes a list of chars
#pre: it's nonempty
#returns same list but with 3 spaces all together
def joinSpaces(s):
	if (len(s) > 0):
		i = len(s) -1 
		while (s[i-1] == ' '):
			i = i - 1
		#now I have the index on the first space of the block of spaces
		wordsGlobal = 1
		while (i < len(s)):
			wordsLoop = wordsGlobal
			iterateSpaces = False
			j = i
			while (wordsLoop > 0):
				if ((s[j-1] == ' ' and iterateSpaces == False) or (s[j-1] != ' ' and iterateSpaces == True)):
					wordsLoop = wordsLoop - 1
					iterateSpaces = not iterateSpaces
				s[j], s[j-1] = s[j-1], s[j]
				s[j], s[j+1] = s[j+1], s[j] 
				j = j - 1
			i = i + 2
			wordsGlobal = wordsGlobal + 2
			
	return s




inputString1 = raw_input('Enter string without extended size:')
inputString2 = list(raw_input('Enter string with extended size: '))
print 'string without extended size with %20: ', separateBy20UsingInsert(inputString1)
print 'string extended size with %20: ', separateBy20UsingSwap(inputString2)