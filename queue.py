"""
Implementation of the Queue abstract data type
"""
class Queue(object):

	def __init__(self):
		self.items = []

	"""
	 Adds a new item to the rear of the queue. 
	 It needs the item as a parameter and returns nothing.
	"""
	def enqueue(self, item):
		self.items.insert(0, item)

	"""
	Removes the front item from the queue. 
	It needs no parameters and returns the item. 
	The queue is modified.
	"""
	def dequeue(self):
		return self.items.pop()

	"""
	Tests to see whether the queue is empty. 
	It needs no parameters and returns a boolean value.
	"""
	def isEmpty(self):
		return self.items == []

	"""
	Returns the number of items in the queue. 
	It needs no parameters and returns an integer.
	"""
	def size(self):
		return len(self.items)
