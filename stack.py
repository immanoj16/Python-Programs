class Node():
	# constructor
	def __init__(self):
		self.data = None
		self.next = None

	# method for setting the data field of the node
	def setData(self, data):
		self.data = data

	# method for getting the data field of the node
	def getData(self):
		return self.data

	# method for setting thenext field of the node
	def setNext(self, next):
		self.next = next

	# method for getting thenext field of the node
	def getNext(self):
		return self.next

	# returns true if the node points to another node
	def hasNext(self):
		return self.next != None

	# Traverse O(n) space O(1)
	def listLength(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.getNext()

		return count
			
	# method for inserting a new node at the beginning of the linked list (at the head)
	def insertAtBeg(self, data):
		newNode = Node()
		newNode.setData(data)

		if self.length == 0:
			self.head = newNode
		else:
			newNode.setNext(self.head)
			self.head = newNode

		self.length += 1

	# method for inserting a new node at the end of a Linked list
	def insertAtEnd(self, data):
		newNode = Node()
		newNode.setData(data)

		current = self.head

		while current.getNext() != None:
			current = current.getNext()

		current.setNext(newNode)
		self.length += 1

	# method for inserting a new node at any position in a linked list
	def insertAtPos(self, data):
		if pos > self.length or pos < 0:
			return None
		else:
			if pos == 0:
				self.insertAtBeg(data)
			else:
				if pos == self.list:
					self.insertAtEnd(data)
				else:
					newNode = Node()
					newNode.setData(data)
					count = 0
					current = self.head
					while count < pos - 1:
						count += 1
						current = current.getNext()

					newNode.setNext(current.getNext())
					current.setNext(newNode)
					self.length += 1

	# method to delete the first node of the linked list
	def deleteFromBeg(self):
		if self.length == 0:
			print "The list is empty"
		else:
			self.head = self.head.hasNext()
			self.length -= 1

	# method to delete the last node of the linked list
	def deleteFromLast(self):
		if self.length == 0:
			print "The list is empty"
		else:
			current = self.head
			previous = self.head

			while current.getNext() != None:
				previous = current
				current = current.getNext()

			previous.setNext(None)
			self.length -= 1
