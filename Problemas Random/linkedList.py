class Node(object):
	def __init__(self, Data, Next, Prev):
		self.data = Data
		self.next = Next
		self.prev = Prev

class DoubleList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def show(self):
		print 'Showing list data: '
		currentNode = self.head
		while currentNode is not None:
			print currentNode.data, '<->'
			currentNode = currentNode.next

	def append(self, data):
		node = Node(data, None, None)
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
			node.prev = self.tail
		self.tail = node

	def delete(self, data):
		currentNode = self.head
		while (currentNode is not None):
			if (currentNode.data == data):
				if (currentNode.prev is not None):
					currentNode.prev.next = currentNode.next
				else:
					self.head = currentNode.next
				if (currentNode.next is not None):
					currentNode.next.prev = currentNode.prev
				else:
					self.tail = currentNode.prev
			
			currentNode = currentNode.next

	def deleteThisOne2(self, node):
		bufferValue = node.data
		node.data = node.next.data
		node.next.data = bufferValue
		if (node.next is self.tail):
			self.tail = node
		
		node.next = node.next.next

	def iterateToNode(self, data):
		currentNode = self.head
		while (currentNode is not None and currentNode.data != data):
			currentNode = currentNode.next
		return currentNode

	def deleteThisOne(self, data):
		self.deleteThisOne2(self.iterateToNode(data))


s = DoubleList()
s.append(31)
s.append(25)
s.append(8)
s.append(10)
s.append(11)
# s.delete(11)
s.deleteThisOne(31)
s.show()

