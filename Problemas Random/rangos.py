def condense_meeting_times(array_of_tuples):
	if len(array_of_tuples) > 1:
		for index, current in enumerate(array_of_tuples[:len(array_of_tuples - 1)]):
			if current[1] >= array_of_tuples[index + 1][0]
				current[1] = array_of_tuples[index + 1][1]
				del array_of_tuples[index + 1] 

	return array_of_tuples



# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
# To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples of integers (start_time, end_time). 
# These integers represent the number of 30-minute blocks past 9:00am.

# For example:

#   (2, 3) # meeting from 10:00 – 10:30 am
# (6, 9) # meeting from 12:00 – 1:30 pm
# Write a function condense_meeting_times() that takes an array of meeting time ranges and returns an array of condensed ranges.

# For example, given:

#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# your function would return:

#   [(0, 1), (3, 8), (9, 12)]
# Do not assume the meetings are in order. The meeting times are coming from multiple teams.

# In this case the possibilities for start_time and end_time are bounded by the number of 30-minute slots in a day. 
# But soon you plan to refactor HiCal to store times as Unix timestamps (which are big numbers). Write something that's efficient 
# even when we can't put a nice upper bound on the numbers representing our time ranges.