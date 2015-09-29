import Queue

def createTeams(li):
	teams = Queue.PriorityQueue()
	for elem in li:
		# print 'inserting: ', elem
		if (teams.empty()):
			teams.put((1, (elem, elem)))
			#show(teams)
		else:
			teamsBuffer = []
			insertedElement = False
			while (not teams.empty() and not insertedElement):
				minorTeam = teams.get()

				if (elem == minorTeam[1][0]-1):
					minorTeam = (minorTeam[0]+1, (minorTeam[1][0]-1, minorTeam[1][1]))
					insertedElement = True 

				elif (elem == minorTeam[1][1]+1):
					minorTeam = (minorTeam[0]+1, (minorTeam[1][0], minorTeam[1][1]+1))
					insertedElement = True

				teamsBuffer.append(minorTeam)

			if (teams.empty() and not insertedElement):
				teams.put((1, (elem, elem)))

			for team in teamsBuffer:
				teams.put(team)
			#show(teams)

	return teams.get()[0]

def show(h):
	elementBuffer = []
	while (not h.empty()):
		element = h.get()
		elementBuffer.append(element)
		print element
	for element in elementBuffer:
		h.put(element)


print 'minor team: ', createTeams([-5, -4, -3, 2, 3, 4, 5, 7])

















# Problem Statement

# For an upcoming programming contest, Roy is forming some teams from the n students of his university. A team can have any number of contestants.

# Roy knows the skill level of each contestant. To make the teams work as a unit, he should ensure that there is no skill gap between the contestants of the same team. In other words, if the skill level of a contestant is x, then he has either the lowest skill level in his team or there exists another contestant with skill level of x-1 in the same team. Also, no two contestants of the same team should have same skill level. Note that a contestant can write buggy code and thus can have a negative skill level.

# The more contestants on the team, the more problems they can attempt at a time. So, Roy wants to form teams such that the smallest team is as large as possible.

# Input Format

# The first line of input contains t (1 <= t <= 100), the number of test cases.

# Each case contains an integer n (0 <= n <= 105), the number of contestants, followed by n space separated integers. The ith integer denotes the skill level of ith contestant. The absolute values of skill levels will not exceed 109.

# The total number of contestants in all cases will not exceed 106.

# Output Format

# For each test case, print the size of smallest team in a separate line.

# Sample Input

# 4  
# 7 4 5 2 3 -4 -3 -5  
# 1 -4  
# 4 3 2 3 1  
# 7 1 -2 -3 -4 2 0 -1  
# Sample Output

# 3
# 1
# 1
# 7
# Explanation

# For the first case, Roy can form two teams: one with contestants with skill levels {-4,-3,-5} and the other one with {4,5,2,3}. The first group containing 3 members is the smallest.

# In the second case, the only team is {-4}

# In the third case, the teams are {3} , {1,2,3}, the size of the smaller group being 1.

# In the last case, you can build a group containing all the contestants. The size of the group equals the total number of contestants.