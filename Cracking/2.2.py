class Node(object):
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next

class SingleList(object):
	head = None
	tail = None

	def show(self):
		print 'Showing list data: '
		currentNode = self.head
		while (currentNode is not None):
			print currentNode.data, '->'
			currentNode = currentNode.next

	def append(self, data):
		newNode = Node(data, None)
		if (self.head is None):
			self.head = newNode
		else:
			self.tail.next = newNode

		self.tail = newNode

	def kthToLast(self, n):
		currentNode = self.head
		i = 0
		while (i < n):
			currentNode = currentNode.next
			i = i + 1
		
		while (currentNode is not None):
			print currentNode.data, '->'
			currentNode = currentNode.next

s = SingleList()
s.append(5)
s.append(10)
s.append(8)
print 'kth(1): '
print s.kthToLast(0)