def classCancelled (k, l):
	return len([e for e in l if e <= 0]) < k

print classCancelled(3, [-1, -3, 4, 2])
print classCancelled(2, [0, -1, 2, 1])


# Problem Statement

# A Discrete Mathematics professor has a class of N students. Frustrated with their lack of discipline, he decides to cancel class if fewer than K students are present when class starts.

# Given the arrival time of each student, determine if the class is canceled.

# Input Format

# The first line of input contains T, the number of test cases.

# Each test case consists of two lines. The first line has two space-separated integers, N (students in the class) and K (the cancelation threshold). 
# The second line contains N space-separated integers (a1,a2,…,aN) describing the arrival times for each student.

# Note: Non-positive arrival times (ai≤0) indicate the student arrived early or on time; positive arrival times (ai>0) indicate the student arrived ai minutes late.

# Output Format

# For each test case, print the word YES if the class is canceled or NO if it is not.