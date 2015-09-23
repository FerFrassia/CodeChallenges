# "Anagram": An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase using all the original letters exactly once; for example, the letters from 'icon' can be rearranged into 'coin'.

# Devise a function that takes one parameter W and returns all the anagrams for W from the file wl.txt.

# anagrams("beat") should return:
# ["beat", "beta", "bate"]

# =====================
# Test cases:

# anagrams("able") should return:
# ['abel', 'able', 'bale', 'beal']

# anagrams("apple") should return:
# ['appel', 'apple']

# anagrams("spot") should return:
# ['post', 'pots', 'spot', 'stop', 'tops']

# anagrams("reset") should return:
# ['reset', 'steer', "trees"]

def anagrams(s1, s2):
	if (len(s1) != len(s2)):
		return False
	else:
		i = 0
		j = 0
		while (i < len(s1)):
			if (s1[i] not in s2 or s2[i] not in s1 or (s1.count(s1[i]) != s2.count(s1[i])) or (s1.count(s2[i]) != s2.count(s2[i]))):
				return False
			i += 1
		return True

def parseN(l):
	i = 0
	while (i < len(l)):
		s = l[i]
		s = s[:-1]
		l[i] = s
		i += 1
	return l

def anagramsInList(word, l):
	returnList = []
	i = 0
	while (i < len(l)):
		if (anagrams(word, l[i])):
			returnList.append(l[i])
		i += 1
	return returnList

fileContent = ''
with open('wl.txt') as f:
	fileContent = f.readlines()

parseN(fileContent)

print 'able: ' + str(anagramsInList('able', fileContent))
print 'apple: ' + str(anagramsInList('apple', fileContent))
print 'post: ' + str(anagramsInList('post', fileContent))
print 'reset: ' + str(anagramsInList('reset', fileContent))




