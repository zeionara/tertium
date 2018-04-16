from enum import Enum

class Color(Enum):
	red = 1
	black = 0

class Node():

	def __init__(self, value, color = Color.black, parent = None, left = None, right = None):
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right
		self.color = color

	def set_parent(self, parent):
		self.parent = parent

	def set_left(self, child):
		self.left = child
		if child:
			child.set_parent(self)

	def set_right(self, child):
		self.right = child
		if child:
			child.set_parent(self)

	def get_uncle(self):
		if self.parent.parent.right == self.parent:
			return self.parent.parent.left
		return self.parent.parent.right

def rotate_right(vertex):

	if vertex.parent:
		if vertex.parent.left == vertex:
			vertex.parent.set_left(vertex.left)
		else:
			vertex.parent.set_right(vertex.left)
	else:
		vertex.left.parent = None

	left_vertex = vertex.left
	vertex.set_left(vertex.left.right)
	left_vertex.set_right(vertex)

def rotate_left(vertex):

	if vertex.parent:
		if vertex.parent.left == vertex:
			vertex.parent.set_left(vertex.right)
		else:
			vertex.parent.set_right(vertex.right)
	else:
		vertex.right.parent = None

	right_vertex = vertex.right
	vertex.set_right(vertex.right.left)
	right_vertex.set_left(vertex)
	

def fixup_after_insert(root, vertex):
	while vertex.parent and vertex.parent.parent:
		uncle_vertex = vertex.get_uncle()
		if uncle_vertex and uncle_vertex.color == Color.red:
			#print('UNCLE IS RED')
			vertex.parent.parent.color = Color.red
			vertex.parent.color = Color.black
			uncle_vertex.color = Color.black
			vertex = vertex.parent.parent
		else:

			if vertex.parent.parent.left == vertex.parent:
				if vertex == vertex.parent.right:
					rotate_left(vertex.parent)
				rotate_right(vertex.parent.parent)
				if vertex.parent:
					vertex.parent.color = Color.black
					if vertex.parent.right:
						vertex.parent.right.color = Color.red
			else:

				if vertex == vertex.parent.left:
					rotate_right(vertex.parent)	
				rotate_left(vertex.parent.parent)
				if vertex.parent:
					vertex.parent.color = Color.black
					if vertex.parent.left:
						vertex.parent.left.color = Color.red
			return
	if vertex.parent:
		vertex = vertex.parent
	vertex.color = Color.black


def insert(root, item):
	previous_vertex = None
	current_vertex = root
	new_vertex = Node(item, Color.red)

	while current_vertex:
		if item < current_vertex.value:
			previous_vertex = current_vertex
			current_vertex = current_vertex.left
		else:
			previous_vertex = current_vertex
			current_vertex = current_vertex.right

	previous_vertex.set_left(new_vertex) if item < previous_vertex.value else previous_vertex.set_right(new_vertex)

	if (previous_vertex.color == Color.red):
		#show_tree(root)
		fixup_after_insert(root, new_vertex)

	return get_root(root)

def get_root(vertex):
	while vertex.parent:
		vertex = vertex.parent
	return vertex

def show_tree(root):
	current_vertex = root
	if current_vertex:
		print(str(current_vertex.value) + ' ' + str(current_vertex.color) + ' ' + str('no' if not current_vertex.parent else current_vertex.parent.value))
		print('left of ' + str(current_vertex.value))
		show_tree(current_vertex.left)
		print('right of ' + str(current_vertex.value))
		show_tree(current_vertex.right)

def build_tree(items):
	root = Node(value = items[0])

	for item in items[1:]:
		root = insert(root, item)

	return root