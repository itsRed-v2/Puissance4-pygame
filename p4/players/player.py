from p4.utils.color import Color

class Player():
	def __init__(self, token, displayName):
		self.token = token
		self.displayName = displayName + Color.RESET