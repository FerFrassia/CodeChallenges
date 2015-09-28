with open ('linksIn.txt') as fin:
	fileContent = fin.read().splitlines()

fout = open('linksOut.txt', 'w')

def detectLinks(li):
	for elem in li:
		if (len(elem) > len('<a href="')):
			i = 0
			while (i < len(elem) - 8):
				window = elem[i:i+9]
				if (window == '<a href="'):
					i += 9
					linkUrl = ''
					while (elem[i] != '"'):
						linkUrl = linkUrl + elem[i]
						i += 1
					while (i < len(elem) - 3):
						window = elem[i:i+4]
						if (window == '</a>'):
							i -= 1
							linkName = ''
							while (elem[i] != '>'):
								linkName = linkName + elem[i]
								i -= 1
							linkName = linkName[::-1]
							totalLink = linkUrl + ',' + linkName + '\n'
							fout.write(totalLink)
							i = len(elem) - 3
						else:
							i += 1
					i = len(elem) - 8
				else:
					i += 1

detectLinks(fileContent)
fout.close()




			
