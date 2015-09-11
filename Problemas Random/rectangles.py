class Rectangle:
	def __init__(self, X = 0, Y = 0, Width = 0, Height = 0):
		self.x = X
		self.y = Y 
		self.width = Width
		self.height = Height

def intersection(a, b):
	rect = Rectangle()
	if (a.x <= b.x <= a.x + a.width):
		rect.x = b.x
		rect.width = min(b.width, a.width - (b.x - a.x))

	elif (b.x <= a.x <= b.x + b.width):
		rect.x = a.x
		rect.width = min(a.width, b.width - (a.x - b.x))
	else:
		raise Exception('No Intersection')

	if (a.y <= b.y <= a.y + a.height):
		rect.y = b.y
		rect.height = min(b.height, a.height - (b.y - a.y))
	elif (b.y <= a.y <= b.y + b.height):
		rect.y = a.y
		rect.height = min(a.height, b.height - (a.y - b.y))
	else:
		raise Exception('No Intersection')

	print 'intersection.x: ', rect.x
	print 'intersection.y: ', rect.y
	print 'intersection.width: ', rect.width
	print 'intersection.height: ', rect.height

r1 = Rectangle(1, 2, 3, 4)

print 'r1.x: ', r1.x
print 'r1.y: ', r1.y
print 'r1.width: ', r1.width
print 'r1.height: ', r1.height

r2 = Rectangle(2, 5, 3, 4)

print 'r2.x: ', r2.x
print 'r2.y: ', r2.y
print 'r2.width: ', r2.width
print 'r2.height: ', r2.height

intersection(r1, r2)



# A crack team of love scientists from OkEros (a hot new dating site) have devised a way 
# to represent dating profiles as rectangles on a two-dimensional plane.
# They need help writing an algorithm to find the intersection of two users love rectangles. 
# They suspect finding that intersection is the key to a matching algorithm so powerful it will cause 
# an immediate acquisition by Google or Facebook or Obama or something.

# It must
# be love
# Write a function to find the rectangular intersection of two given love rectangles.

# As with the example above, love rectangles are always "straight" and never "diagonal." 
# More rigorously: each side is parallel with either the x-axis or the y-axis.







