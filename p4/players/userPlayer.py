from p4.players.player import Player
from p4.utils.color import Color

from p4.display.helpMenu import displayHelp

class UserPlayer(Player):
	def __init__(self, token, displayName, view, stopHook):
		self.view = view
		self.stopHook = stopHook
		super().__init__(token, displayName)

	def play(self, board, input = input, displayHelp = displayHelp):
		while True:
			reponse = input("-> ").strip()

			if reponse == "": pass

			elif reponse == "stop":
				self.stopHook()
				return None

			elif reponse == "help":
				displayHelp()

			elif reponse.isdecimal():
				value = int(reponse)

				if value < 1 or value > board.WIDTH:
					self.view.footer = Color.RED + "Il n'y a pas de colonne n°" + reponse
				elif board.getFirstEmpty(value - 1) == -1:
					self.view.footer = Color.RED + "Cette colonne est pleine!"
				else:
					return value

			else:
				self.view.footer = Color.RED + "Argument invalide: " + repr(reponse)
			
			self.view.displayGame(self.displayName)