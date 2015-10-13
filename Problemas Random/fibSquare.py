def fib_square(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		fib_prev_prev = 0
		fib_prev = 1
		i = 2
		while (i != n):
			val = fib_prev**2 + fib_prev_prev
			fib_prev_prev = fib_prev
			fib_prev = val
			i += 1
		return fib_prev


for i in range(10):
	print fib_square(i)
