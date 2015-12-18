def utopianTree(n):
	height = 1
	duplicates = True
	while n != 0:
		if duplicates:
			height = height*2
		else:
			height += 1

		duplicates = not duplicates
		n -= 1

	return height

print utopianTree(4)

# The Utopian Tree goes through 2 cycles of growth every year. 
# Each spring, it doubles in height. Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. 
# How tall will her tree be after N growth cycles?