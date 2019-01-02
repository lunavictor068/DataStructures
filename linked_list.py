class Node:

	def __init__(self, data = None):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = Node()

	def append(self, data):
		temp = self.head
		while temp.next != None:
			temp = temp.next
		temp.next = Node(data)

	def length(self):
		temp = self.head
		length = 0
		while temp.next != None:
			length += 1
			temp = temp.next
		return length

	def display(self):
		elements = []
		temp = self.head
		while temp.next != None:
			temp = temp.next
			elements.append(temp.data)
		print(elements)

	def get_at(self, index):
		if index < 0 or index >= self.length():
			print("ERROR: index out of range")
			return None
		current_index = 0
		current_node = self.head
		while True:
			current_node = current_node.next
			if current_index == index:
				return current_node.data
			current_index += 1

	def remove_at(self, index):
		if index < 0 or index >= self.length():
			print("ERROR: index out of range")
			return
		current_index = 0
		current_node = self.head
		while True:
			temp = current_node
			current_node = current_node.next
			if current_index == index:
				temp.next = current_node.next
				return
			current_index += 1

