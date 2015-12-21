k = 0

def ciphered(s, rotate):
	global k
	k = rotate
	# print 'ord(a): ' + str(ord('a'))
	# print 'ord(z): ' + str(ord('z'))
	# print 'ord(A): ' + str(ord('A'))
	# print 'ord(Z): ' + str(ord('Z'))
	return ''.join(map(newChar, list(s)))

def newChar(c):
	if 97 <= ord(c) and ord(c) <= 122:
		return chr(((ord(c)+ k - 97) % 26)+97)
	elif 65 <= ord(c) and ord(c) <= 90:
		return chr(((ord(c)+ k - 65) % 26)+65)
	else:
		return c


print ciphered('middle-Outz', 2)

# Problem Statement

# Julius Caesar protected his confidential information by encrypting it in a cipher. 
# Caesar''s cipher rotated every letter in a string by a fixed number, K, making it unreadable by his enemies. 
# Given a string, S, and a number, K, encrypt S and print the resulting string.

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Input Format

# The first line contains an integer, N, which is the length of the unencrypted string. 
# The second line contains the unencrypted string, S. 
# The third line contains the integer encryption key, K, which is the number of letters to rotate.