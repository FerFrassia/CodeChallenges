# l = [[1, 5, 8, 9], [2, 3, 7, 10], [4, 6, 11, 15], [9, 14, 16, 19], [2, 4, 6, 9]]
import Queue

def kwWayMerge(l):
	minheap = Queue.PriorityQueue()
	for e in l:
		node = (e[0], (0, e))
		minheap.put(node)

	merge = []
	while (not minheap.empty()):
		top = minheap.get()
		merge.append(top[0])
		if (top[1][0] < len(top[1][1])-1):
			top = (top[1][1][top[1][0]+1], (top[1][0]+1, top[1][1]))
			minheap.put(top)

	return merge

def bruteForce(l):
	merge = []
	i = 0
	while (i < len(l)):
		for e in l[i]:
			merge.append(e)
		i += 1

	return sorted(merge)

def show(q):
	while (not q.empty()):
		print q.get()

print 'kWayMerge: ' + str(kwWayMerge([[1, 5, 8, 9], [2, 3, 7, 10], [4, 6, 11, 15], [9, 14, 16, 19], [2, 4, 6, 9]]))
print 'brute for: ' + str(bruteForce([[1, 5, 8, 9], [2, 3, 7, 10], [4, 6, 11, 15], [9, 14, 16, 19], [2, 4, 6, 9]]))

