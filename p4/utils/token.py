import enum

class Token(enum.Enum):
	YELLOW = "yellow"
	BLUE = "blue"
	EMPTY = "empty"

	def getOpposite(token):
		if token == Token.YELLOW:
			return Token.BLUE
		elif token == Token.BLUE:
			return Token.YELLOW
		return None