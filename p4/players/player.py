from p4.utils.color import Color
from p4.utils.token import Token

class Player():
	def __init__(self, token: Token, displayName):
		self.token = token
		self.displayName = displayName + Color.RESET