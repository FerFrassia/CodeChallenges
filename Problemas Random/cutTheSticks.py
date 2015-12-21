def cutTheSticks(l):
	l = sorted(l)
	i = 0
	shortestStick = None
	while i < len(l):
		if shortestStick is None or l[i] != shortestStick:
			shortestStick = l[i]
			print len(l)-i
		i += 1

print cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1])











# Problem Statement

# You are given N sticks, where the length of each stick is a positive integer. 
# A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

# Suppose we have six sticks of the following lengths:
# 5 4 4 2 2 8

# Then, in one cut operation we make a cut of length 2 from each of the six sticks. 
# For the next cut operation four sticks are left (of non-zero length), whose lengths are the following: 
# 3 2 2 6

# The above step is repeated until no sticks are left.

# Given the length of N sticks, print the number of sticks that are left before each subsequent cut operations.

# Note: For each cut operation, you have to recalcuate the length of smallest sticks (excluding zero-length sticks).