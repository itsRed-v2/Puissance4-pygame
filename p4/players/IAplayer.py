from typing import Callable
from random import randint

from p4.players.player import Player
from p4.board import Board

from p4.strikeDetector import detectStrike
from p4.utils.vector import Vector
from p4.utils.token import Token

class Column():
	def __init__(self, number: int) -> None:
		self.index = number
		self.score = 0

class Task():
	def __init__(self, delay: int, method: Callable) -> None:
		self.delay = delay
		self.execute = method

class IAPlayer(Player):
	def __init__(self, token: Token, displayName):
		self.taskList: list[Task] = []
		super().__init__(token, displayName)

	def tick(self):
		for task in self.taskList:
			task.delay -= 1
			if task.delay == 0:
				task.execute()
				self.taskList.remove(task)

	def executeLater(self, delay: int, method: Callable):
		self.taskList.append(Task(delay, method))

	def play(self, board: Board, playCB: Callable):
		# Initialisation
		oppositeToken = self.token.getOpposite()

		playable = []
		for i in range(board.WIDTH):
			playable.append(Column(i))

		# Suppression des colonnes pleines

		def filterFull(col):
			firstEmpty = board.getFirstEmpty(col.index)
			return firstEmpty != None and firstEmpty != -1

		playable = list(filter(filterFull, playable))

		for col in playable:
			index = col.index
			firstEmpty = board.getFirstEmpty(index)
			assert firstEmpty != None
			pos = Vector(index, firstEmpty)
			upPos = Vector(index, firstEmpty - 1)

			# Joue les coups qui font gagner
			if detectStrike(board, pos, self.token):
				col.score += 10000
		
			# Bloque les lignes de l'adversaire
			if detectStrike(board, pos, oppositeToken):
				col.score += 200

			# Ne joue pas à un endroit qui permet à l'adversaire de gagner
			if detectStrike(board, upPos, oppositeToken):
				col.score -= 200
			
			# Ne joue pas à un endroit qui permet à l'adversaire de le bloquer
			if detectStrike(board, upPos, self.token):
				col.score -= 10

		# Selection du plus haut score

		best = []
		for col in playable:
			if len(best) == 0 or col.score > best[0].score:
				best = [col]
			elif col.score == best[0].score:
				best.append(col)

		# Choisis au hasard parmi les possibilités identiques
		finalAnswer = best[randint(0, len(best) - 1)].index
		
		def finish():
			playCB(finalAnswer)
		self.executeLater(30, finish)
		
