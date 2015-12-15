def logaritmicPower(a, b):
	if b == 1:
		return a
	else:
		leftB = b/2
		rightB = b/2
		
		if leftB + rightB != b:
			leftB += 1

		return logaritmicPower(a, leftB) * logaritmicPower(a, rightB)

print logaritmicPower(3, 6)

