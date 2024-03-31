from linkednode import LinkedNode
#from linkedlist import LinkedList

class LinkedStack:
	def __init__(self):
		#self.stack = []
		self._top = None
		self._size = 0

	def push(self, value):
		node = LinkedNode(value, self._top)
		self._top = node
		self._size += 1

	def __str__(self):
		string_return = "LinkedStack(["
		current = self._top
		while current != None:
			string_return += str(current.data)

			if current.tail != None:
				current = current.tail
				string_return += ", "
			else:
				current = None

		return string_return + "])"

	def pop(self):
		if self._top == None:
			raise ValueError('Stack is empty!')
		else:
			temp = self._top
			self._top = self._top.tail
			self._size -= 1
			return temp.data

	def peek(self):
		if self._top == None:
			return None
		else:
			return self._top.data

	def __len__(self):
		return self._size

	def isempty(self):
		if self._top == None:
			return True
		else:
			return False

########################################################
########################################################
########################################################

class LinkedQueue:
	def __init__(self):
		self._front = None
		self._back = None
		self._size = 0

	def enqueue(self, value):
		node = LinkedNode(value)
		if self._front == None:	
			self._front = node
			self._back = node
			
		else:
			self._back.tail = node
			self._back = node

		self._size += 1

	def __str__(self):
		string_return = "LinkedQueue(["
		current = self._front
		while current != None:
			string_return += str(current.data)

			if current.tail != None:
				current = current.tail
				string_return += ", "
			else:
				current = None

		return string_return + "])"

	def pop(self):
		if self._front == None:
			raise ValueError('Queue is empty!')
		else:
			temp = self._front
			self._front = self._front.tail
			self._size -= 1
			return temp.data

	def peek(self):
		if self._front == None:
			return None
		else:
			return self._front.data

	def __len__(self):
		return self._size

	def isempty(self):
		if self._front == None:
			return True
		else:
			return False

queue = LinkedQueue()
print(queue.isempty())
queue.enqueue(1)
print(queue)
queue.enqueue(2)
print(queue)
queue.enqueue(3)
print(queue)
queue.pop()
print(queue.peek())
print(queue)
print(queue.isempty())
print(len(queue))


