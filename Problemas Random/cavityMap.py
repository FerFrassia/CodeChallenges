def cavities(l):
	for c, column in enumerate(l):
		for r, row in enumerate(column):
			row = str(row)
			if c != 0 and c != len(l)-1 and r != 0 and r != len(column)-1:
				# check for cavity
				if column[r-1] < row and row > column[r+1] and l[c-1][r] < row and row > l[c+1][r]:
					column[r] = 'X'
	return l
				


print cavities([[1, 1, 1, 2], [1, 9, 1, 2], [1, 8, 9, 2], [1, 2, 3, 4]])



# Problem Statement

# You are given a square map of size nxn. Each cell of the map has a value denoting its depth. 
# We will call a cell of the map a cavity if and only if this cell is not on the border of the map 
# and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

# You need to find all the cavities on the map and depict them with the uppercase character X.

# Input Format

# The first line contains an integer, n, denoting the size of the map. 
# Each of the following n lines contains n positive digits without spaces. 
# Each digit (1-9) denotes the depth of the appropriate area.

