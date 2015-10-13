def max_subarray(l):
	current_sum = 0
	best_sum = 0
	current_index = -1
	best_start_index = -1
	best_end_index = -1
	i = 0
	while (i < len(l)):
		val = current_sum + l[i]
		if (val > 0):
			if current_sum == 0:
				current_index = i
			current_sum = val
		else:
			current_sum = 0

		if (current_sum > best_sum):
			best_sum = current_sum
			best_start_index = current_index
			best_end_index = i

		i += 1

	return l[best_start_index:best_end_index+1]

def max_subarray_not_necesarilly_joined(l):
	total_sum = 0
	i = 0
	while (i < len(l)):
		if (l[i] > 0):
			total_sum += l[i]
		i += 1
	return total_sum

print max_subarray_not_necesarilly_joined([2, -1, -100, 2, 3, 4, 5])


