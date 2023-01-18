from random import randint
from time import sleep

from p4.players.player import Player
from p4.board import Board

from p4.strikeDetector import detectStrike
from p4.utils.vector import Vector
from p4.utils.token import Token

class Column():
	def __init__(self, number: int) -> None:
		self.index = number
		self.score = 0

class IAPlayer(Player):
	def play(self, board: Board, randint = randint, doSleep: bool = True) -> int:
		if doSleep: sleep(.5)

		oppositeToken = Token.getOpposite(self.token)

		# Initialisation

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

		# debug
		# st = ""
		# for i in range(7):
		# 	for col in playable:
		# 		if col.index == i:
		# 			st += f"{col.score:+5d}"
		# 			break
		# 	else:
		# 		st += "____"
		# 	st += " | "
		# print(st)
		##

		# Choisis au hasard parmi les possibilités identiques
		return best[randint(0, len(best) - 1)].index + 1
