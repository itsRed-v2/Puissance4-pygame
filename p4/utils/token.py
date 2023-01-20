import enum

class Token(enum.Enum):
	YELLOW = "yellow"
	BLUE = "blue"
	EMPTY = "empty"

	def getOpposite(self):
		assert self != Token.EMPTY # This method should not be called on an empty token

		if self == Token.YELLOW:
			return Token.BLUE
		else:
			return Token.YELLOW