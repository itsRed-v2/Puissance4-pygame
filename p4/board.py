from p4.utils.token import Token
from p4.utils.vector import Vector

class Board:
	def __init__(self, stringRows = None, height = 6, width = 7):
		self.columns: list[list[Token]] = []
		self.lastTokenPos = None
		self.streaks: list[list[Vector]] = [] # List of all the 4+ lines of same-colour tokens
		self.HEIGHT = height
		self.WIDTH = width
		
		for c in range(self.WIDTH):
			column = []
			for l in range(self.HEIGHT):

				if stringRows != None:
					
					if stringRows[l][c] == 'B':
						column.append(Token.BLUE)
					elif stringRows[l][c] == 'Y':
						column.append(Token.YELLOW)
					else: column.append(Token.EMPTY)

				else: column.append(Token.EMPTY)

			self.columns.append(column)
	
	def getColumn(self, index: int):
		if 0 <= index < self.WIDTH:
			return self.columns[index]
	
	def getTokenAt(self, col: int, row: int):
		return self.columns[col][row]

	def addToken(self, columnIndex, token: Token):
		column = self.getColumn(columnIndex)
		assert column != None

		row = self.getFirstEmpty(columnIndex)
		assert row != None and row != -1

		column[row] = token
		self.lastTokenPos = Vector(columnIndex, row)

		streaks = self.detectStreaks(self.lastTokenPos, token)
		self.streaks += streaks
	
	def getFirstEmpty(self, columnIndex: int):
		column = self.getColumn(columnIndex)
		if column == None: return None

		for row in range(len(column) - 1, -1, -1): # This ranges from len(column)-1 to 0
			if column[row] == Token.EMPTY:
				return row
		return -1
	
	def detectStreaks(self, pos: Vector, token: Token):
		directions = [
			Vector(1, 1),
			Vector(0, 1),
			Vector(-1, 1),
			Vector(1, 0)
		]

		streaks = []

		for direction in directions:
			result = self.is4Line(pos, direction, token)
			if result != None:
				streaks.append(result)
		
		return streaks

	def is4Line(self, pos: Vector, direction: Vector, token: Token):
		points = self.findLine(pos, direction, token)
		points.reverse()

		points.append(Vector(pos.c, pos.r))

		direction.multiply(-1)
		points += self.findLine(pos, direction, token)
		
		if len(points) >= 4:
			return points
		return None

	def findLine(self, pos: Vector, direction: Vector, token: Token):
		points: list[Vector] = []

		pointer = Vector(pos.c, pos.r)
		pointer.add(direction)
		
		while (0 <= pointer.c < self.WIDTH
				and 0 <= pointer.r < self.HEIGHT
				and self.getTokenAt(pointer.c, pointer.r) == token):

			points.append(Vector(pointer.c, pointer.r))

			pointer.add(direction)
		
		return points