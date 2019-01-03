class Node:
	def __init__(self, value = None):

		self.value = value
		self.left_child = None
		self.right_child = None
		self.parent = None


class BST:

	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, current_node):
		if value < current_node.value:
			if current_node.left_child == None:
				current_node.left_child = Node(value)
				current_node.left_child.parent = current_node
			else:
				self._insert(value, current_node.left_child)
		elif value > current_node.value:
			if current_node.right_child == None:
				current_node.right_child = Node(value)
				current_node.right_child.parent = current_node
			else:
				self._insert(value, current_node.right_child)
		else:
			print(value, "already in tree.")

	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)

	def height(self):
		if self.root != None:
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, current_node, current_height):
		if current_node == None:
			return current_height
		left_height = self._height(current_node.left_child, current_height + 1)
		right_height = self._height(current_node.right_child, current_height + 1)
		return max(left_height, right_height)

	def search(self, value):
		if self.root != None:
			return self._search(value, self.root)
		else:
			return False

	def find(self):
		if self.root != None:
			return self._find(value, self.root)
		else:
			return None

	def _find(self):
		if value == current_node.value:
			return current_node
		elif value < current_node.value and current_node.left_child != None:
			return self._find(value, current_node.left_child)
		elif value > current_node.value and current_node.right_child != None:
			return self._find(value, current_node.right_child)

	def delete_value(self, value):
		return self.delete_node(self.find(value))

	def delete_node(self, node):

		def min_value_node(n):
			current = n
			while current.left_child != None:
				current = current.left_child
			return current

		def num_children(n):
			num_children = 0
			if n.left_child != None:
				num_children += 1
			if n.right_child != None:
				return num_children

		node_parent = node.parent
		node_children = num_children(node)
		if node_children == 0:
			if node_parent.left_child == node:
				node_parent.left_child = None
			else:
				node_parent.right_child= None
		elif node_children == 1:
			if node.left_child != None:
				child = node.left_child
			else:
				child = node.right_child
			if node_parent.left_child == node:
				node_parent.left_child = child
			else:
				node_parent.right_child = child
			child.parent = node_parent
		elif node_children == 2:
			successor = min_value_node(node.right_child)
			node.value = successor.value
			self.delete_node(successor)

	def _search(self, value, current_node):
		if value == current_node.value:
			return True
		elif value < current_node.value and current_node.left_child != None:
			return self._search(value, current_node.left_child)
		elif value > current_node.value and current_node.right_child != None:
			return self._search(value, current_node.right_child)
		return False

	def _print_tree(self, current_node):
		if current_node != None:
			self._print_tree(current_node.left_child)
			print(str(current_node.value))
			self._print_tree(current_node.right_child)
