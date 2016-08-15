class Stack(object):

	def __init__(self):
		self.items = []

	def __str__(self):
		return ("Stack of size %d" % len(self.items))

	"""
	Tests to see whether the stack is empty. 
	It needs no parameters and returns a boolean value.
	"""
	def isEmpty(self):
		return self.items == []

	"""
	Adds a new item to the top of the stack. 
	It needs the item and returns nothing.
	"""
	def push(self, item):
		self.items.append(item)

	"""
	Removes the top item from the stack. 
	It needs no parameters and returns the item. 
	The stack is modified.
	"""
	def pop(self):
		if self.size() <= 0:
			return None
		return self.items.pop()

	"""
	Returns the top item from the stack but does not remove it. 
	It needs no parameters. 
	The stack is not modified.
	"""
	def peek(self):
		if self.isEmpty():
			return None
		return self.items[len(self.items) - 1]

	"""
	Returns the number of items on the stack. 
	It needs no parameters and returns an integer.
	"""
	def size(self):
		return len(self.items)
