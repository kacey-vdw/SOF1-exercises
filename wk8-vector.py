class Vector():

	def __init__(self, *numbers): #= None):
		if numbers != None: #if a value was given
			self._vector = []
			for value in numbers:
				if isinstance(value, list):
					for number in value:
						self._vector.append(number)
				else:
					self._vector.append(value)
		else: #if no value given
			self._vector = [] #set as empty list

	def __str__(self):
		vector_string = "<"
		for item in self._vector:
			vector_string += str(float(item))
			if item != self._vector[-1]:
				vector_string += ", "
		return vector_string + ">"

	def dim(self):
		return len(self._vector)

	def get(self, index: int):
		return self._vector[index]

	def set(self, index: int, value: float):
		self._vector[index] = value

	def scalar_product(self, scalar):
		new_vector = []
		for item in self._vector:
			new_vector.append(round(float(item*scalar),1))
		return Vector(new_vector)

	def add(self, other_vector):
		if not isinstance(other_vector , Vector):
			raise TypeError
		elif other_vector.dim() != len(self._vector):
			raise ValueError
		else:
			sum_vector = []
			for index in range(0, other_vector.dim()):
				sum_vector.append(other_vector.get(index) + self._vector[index])
			return Vector(sum_vector)

	def equals(self, other_vector):
		#if other_vector == None or self._vector == None:
			#return False
		if not isinstance(other_vector , Vector):
			return False
		elif other_vector.dim() != len(self._vector):
			return False
		else:
			for index in range(0, other_vector.dim()):
				if other_vector.get(index) !=self._vector[index]:
					return False
		return True

	def __eq__(self, other_vector):
		#if other_vector == None or self._vector == None:
			#return False
		if not isinstance(other_vector , Vector):
			return False
		elif other_vector.dim() != len(self._vector):
			return False
		else:
			for index in range(0, other_vector.dim()):
				if other_vector.get(index) !=self._vector[index]:
					return False
		return True

	def __ne__(self, other_vector):
		if other_vector == None or self._vector == None:
			return True
		if not isinstance(other_vector , Vector):
			return True
		elif other_vector.dim() != len(self._vector):
			return True
		else:
			for index in range(0, other_vector.dim()):
				if other_vector.get(index) !=self._vector[index]:
					return True
		return False

	def __add__(self, other_vector):
		if not isinstance(other_vector , Vector):
			raise TypeError
		elif other_vector.dim() != len(self._vector):
			raise ValueError
		else:
			sum_vector = []
			for index in range(0, other_vector.dim()):
				sum_vector.append(other_vector.get(index) + self._vector[index])
			return Vector(sum_vector)

	def __mul__(self, scalar):
		raise TypeError


	def __rmul__(self, scalar):
		new_vector = []
		for item in self._vector:
			new_vector.append(round(float(item*scalar),1))
		return Vector(new_vector)

	def __imul__(self, scalar):
		new_vector = []
		for item in self._vector:
			new_vector.append(round(float(item*scalar),1))
		return Vector(new_vector)

	def __iadd__(self, other_vector):
		if not isinstance(other_vector , Vector):
			raise TypeError
		elif other_vector.dim() != len(self._vector):
			raise ValueError
		else:
			sum_vector = []
			for index in range(0, other_vector.dim()):
				sum_vector.append(other_vector.get(index) + self._vector[index])
			return Vector(sum_vector)

	def __getitem__(self, index):
		if index < -1 or index > len(self._vector):
			return ValueError
		else:
			return self._vector[index]

	def __setitem__(self, index, value):
		#if index < 0 or index > len(self._vector):
			#return ValueError
		self._vector[index] = value


v1 = Vector([1,2,3])
v2 = Vector([1,2,3])
#print(v1.equals(v2)) #True
#v3 = Vector([0,2,0])
#print(v3.equals(v1)) #False
#print(v1 == v2) #False
#print(v1 * 3)
#print(2 * v1)
#print(v1[0])
v1[2] += 3
print(v1)
