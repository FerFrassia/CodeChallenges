class Node(object):
	def __init__(self, Data, Next):
		self.data = Data
		self.next = Next

class SingleList(object):
	head = None
	tail = None

	def show(self):
		print 'showing list data: '
		currentNode = self.head
		while (currentNode is not None):
			if (currentNode is self.tail):
				print currentNode.data
			else:
				print currentNode.data, '->'
			currentNode = currentNode.next

	def append(self, data):
		newNode = Node(data, None)
		if (self.head is None):
			self.head = newNode
		else:
			self.tail.next = newNode
		self.tail = newNode

	def delete(self, data):
		currentNode = self.head
		if (currentNode.data == data):
			self.head = currentNode.next
			if (self.tail is currentNode):
				self.tail = None
		else:
			while (currentNode.next.data != data):
				currentNode = currentNode.next

			if (currentNode.next is self.tail):
				self.tail = currentNode

			currentNode.next = currentNode.next.next

	def deleteRepeated(self):
		repeatedSet = set()
		currentNode = self.head
		iteration = 0
		while (currentNode is not None):
			if (currentNode.data in repeatedSet):
				self.delete(currentNode.data)
			else:
				repeatedSet.add(currentNode.data)
			currentNode = currentNode.next
			iteration += 1


s = SingleList()
s.append(5)
s.append(10)
s.append(20)
s.append(10)
s.append(10)
s.append(50)
s.append(20)
s.deleteRepeated()
s.show()



















