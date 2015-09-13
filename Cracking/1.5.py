def compressed(s):
	if (len(s) < 2):
		return s
	else:
		s = list(s)
		newString = ''
		i = 0
		j = i
		while (j < len(s) - 1):
			if (s[j] != s[j+1]):
				newString += s[j]
				newString += str(j-i+1)
				i = j+1

				if (j+1 == len(s)-1):
					newString += s[j+1]
					newString += str(1)
			else:
				if (j+1 == len(s)-1):
					newString += s[j]
					newString += str(j+1-i+1)

			j = j + 1

	if (len(newString) > len(s)):
		return ''.join(s)
	else:
		return newString

inputString = raw_input('Enter string: ')
print 'compressed: ', compressed(inputString)
