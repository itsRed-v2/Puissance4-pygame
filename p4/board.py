from p4.utils.token import Token
from p4.utils.vector import Vector

class Board:
	def __init__(self, stringRows = None, height = 6, width = 7):
		self.columns: list[list[Token]] = []
		self.lastTokenPos = None
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

	def addToken(self, columnIndex, token: Token):
		column = self.getColumn(columnIndex)
		if column == None: return None

		row = self.getFirstEmpty(columnIndex)
		if row != None and row != -1:
			column[row] = token
			self.lastTokenPos = Vector(columnIndex, row)

		return row
	
	def getFirstEmpty(self, columnIndex: int):
		column = self.getColumn(columnIndex)
		if column == None: return None

		for row in range(len(column) - 1, -1, -1): # This ranges from len(column)-1 to 0
			if column[row] == Token.EMPTY:
				return row
		return -1