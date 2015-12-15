def fillMatrix(m, tY, tX, tVal, x0, x1, y0, y1):

	#base case, 2x2 matrix 
	if x0+1 == x1 and y0+1 == y1:
		
		m[x0][y0] = tVal+1
		m[x1][y0] = tVal+1
		m[x0][y1] = tVal+1
		m[x1][y1] = tVal+1

		m[tX][tY] = tVal
	
	else:
		
		midX = x0 + (x1-x0)/2
		midY = y0 + (y1-y0)/2

		#case target is in first cuadrant
		if tX <= midX and tY <= midY:

			#first
			fillMatrix(m, tX, tY, tVal, x0, midX, y0, midY)
			
			#second
			tVal += ((midX-x0) ** 2 - 1) / 3 + 2
			fillMatrix(m, midX+1, midY, tVal, midX+1, x1, y0, midY)

			#third
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX+1, midY+1, tVal, midX+1, x1, midY+1, y1)

			#fourth
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX, midY+1, tVal, x0, midX, midY+1, y1)

		#case target is in second cuadrant
		elif tX > midX and tY <= midY:

			#second
			fillMatrix(m, tX, tY, tVal, midX+1, x1, y0, midY)

			#third
			tVal += ((midX-x0) ** 2 - 1) / 3 + 2
			fillMatrix(m, midX+1, midY+1, tVal, midX+1, x1, midY+1, y1)

			#fourth
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX, midY+1, tVal, x0, midX, midY+1, y1)

			#first
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX, midY, tVal, x0, midX, y0, midY)

		#case target is in third cuadrant
		elif tX > midX and tY > midY:

			#third
			fillMatrix(m, tX, tY, tVal, midX+1, x1, midY+1, y1)

			#fourth
			tVal += ((midX-x0) ** 2 - 1) / 3 + 2
			fillMatrix(m, midX, midY+1, tVal, x0, midX, midY+1, y1)

			#first
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX, midY, tVal, x0, midX, y0, midY)

			#second
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX+1, midY, tVal, midX+1, x1, y0, midY)

		#case target is in fourth cuadrant
		else:

			#fourth
			fillMatrix(m, tX, tY, tVal, x0, midX, midY+1, y1)

			#first
			tVal += ((midX-x0) ** 2 - 1) / 3 + 2
			fillMatrix(m, midX, midY, tVal, x0, midX, y0, midY)

			#second
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX+1, midY, tVal, midX+1, x1, y0, midY)

			#third
			tVal += ((midX-x0) ** 2 - 1) / 3 + 1
			fillMatrix(m, midX+1, midY+1, tVal, midX+1, x1, midY+1, y1)

	return m


def showMatrix(m):
	for e in m:
		print e


m = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
showMatrix(fillMatrix(m, 1, 0, 0, 0, 3, 0, 3))











#cuadrants:
#  1 | 2
#  ------
#  4 | 3
#
#