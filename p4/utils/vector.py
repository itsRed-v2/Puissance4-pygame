class Vector:
	def __init__(self, c, r):
		self.c = c
		self.r = r
	
	def add(self, vec):
		self.c += vec.c
		self.r += vec.r
	
	def subtract(self, vec):
		self.c -= vec.c
		self.r -= vec.r
	
	def multiply(self, number):
		self.c *= number
		self.r *= number

	def asTuple(self):
		return (self.c, self.r)
	
	def __eq__(self, other): 
		if not isinstance(other, Vector):
			return False
		
		return self.c == other.c and self.r == other.r