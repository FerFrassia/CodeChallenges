def compress(s):
	i = 0
	startIndex = 0
	compressed = ''
	while i < len(s):
		if s[i] != s[startIndex] or (i == len(s)-1 and s[i] == s[startIndex]):
			if i == len(s)-1 and s[i] == s[startIndex]:
				i += 1
			newString = ''
			if i - startIndex > 3:
				newString = s[startIndex] + '*' + str(i-startIndex)
			else:
				newString = s[startIndex] * (i-startIndex)
			compressed = compressed + newString
			print compressed
			startIndex = i

		i += 1

	return compressed

print compress('aabC12Kkkkjjjj00rrrrrr')
