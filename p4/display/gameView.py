import os

from p4.utils.color import Color
from p4.utils.token import Token
from p4.utils.vector import Vector

from p4.board import Board

tokenColors = {
	Token.YELLOW: Color.YELLOW,
	Token.BLUE: Color.BLUE,
	Token.EMPTY: Color.GRAY
}

class View:
	def __init__(self, board: Board):
		self.board = board
		self.footer = ""
		self.highlightedPoints = []

	def displayBoard(self):
		
		line = "|" + Color.BOLD
		for i in range(self.board.WIDTH):
			line += str(i + 1).rjust(2, " ") + " "
		line += Color.RESET + "|"
		print(line)

		for row in range(self.board.HEIGHT):
			line = Color.RESET + "|"

			for col in range(self.board.WIDTH):
				line += Color.RESET

				token = self.board.getColumn(col)[row]
				line += tokenColors.get(token)

				symbol = "O"

				pointer = Vector(col, row)
				lastToken = self.board.lastTokenPos
				if pointer == lastToken:
					line += Color.BOLD
					symbol = "0"

				if self.highlightedPoints.count(pointer) >= 1:
					symbol = "X"

				line += f" {symbol} "
				
			line += Color.RESET + "|"
			
			print(line)

	def displayGame(self, playerName):
		header = f"C'est au tour de {playerName}"
		permFooter = "Entrez \"help\" pour de l'aide"
		self.display(header, permFooter)
	
	def display_win(self, playerName):
		header = ""
		permFooter = f"{playerName} a gagné!"
		self.display(header, permFooter)
	
	def display(self, header, permFooter):
		print(Color.RESET)

		size = os.get_terminal_size()
		for i in range(size.lines - 6 - self.board.HEIGHT):
			print("")

		print(header + Color.RESET)

		self.displayBoard()

		print(self.footer + Color.RESET)
		print(permFooter)

		self.footer = ""