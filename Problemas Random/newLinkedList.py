class Node(object):
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, data):
		newNode = Node(data, None)
		if (self.head is None):
			self.head = newNode
		else:
			self.tail.next = newNode

		self.tail = newNode
		self.size += 1

	def show(self):
		currentNode = self.head
		while (currentNode is not None):
			if (currentNode is self.head):
				print 'head'
			if (currentNode is self.tail):
				print 'tail'
			print currentNode.data
			currentNode = currentNode.next

	def deleteAllRepetitions(self, data):
		if (self.head is not None):
			currentNode = self.head
			while (currentNode is not None):
				if (currentNode is self.head and currentNode.data == data):
					self.head = currentNode.next
				else:
					if (currentNode.next.data == data):
						iteratingNode = currentNode.next
						while (iteratingNode is not None and iteratingNode.data == data):
							iteratingNode = iteratingNode.next

						currentNode.next = iteratingNode
						if (iteratingNode is None):
							self.tail = currentNode

				currentNode = currentNode.next
				if (currentNode is self.tail):
					currentNode = None


l = LinkedList()
l.append(10)
l.append(5)
l.append(5)
l.append(10)
l.show()
l.deleteAllRepetitions(5)
print '\n'
l.show()
