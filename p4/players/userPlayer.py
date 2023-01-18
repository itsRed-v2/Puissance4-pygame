from typing import Callable

from p4.players.player import Player
from p4.board import Board

class UserPlayer(Player):
	def __init__(self, token, displayName):
		super().__init__(token, displayName)

	# def play(self, board: Board, callback: Callable):
	# 	def onInput(colIndex):
	# 		if board.getFirstEmpty(colIndex) == -1:
	# 			self.interface.awaitUserInput(onInput)
	# 		else:
	# 			callback(colIndex)

	# 	self.interface.awaitUserInput(onInput)
		