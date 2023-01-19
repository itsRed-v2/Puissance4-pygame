import sys
import pygame

from p4.players.IAplayer import IAPlayer
from p4.players.userPlayer import UserPlayer

from p4.board import Board
from p4.utils.token import Token
from p4.utils.vector import Vector
from p4.utils.color import Color

from p4.display.interface import Interface

from p4.strikeDetector import detectStrike

pygame.init()
pygame.display.set_caption("Puissance 4")

board = Board()

# Custom sized board
if len(sys.argv) == 3:
	h = sys.argv[1]
	w = sys.argv[2]
	
	if h.isdecimal() and w.isdecimal():
		board = Board(height = int(h), width = int(w))
# ==

interface = Interface(board)

playing = True

def stopGame():
	global playing
	playing = False

USER = UserPlayer(Token.YELLOW, Color.YELLOW + "Utilisateur")
IA = IAPlayer(Token.BLUE, Color.BLUE + "Ordi")

# def play(player):
# 	answer = player.play(board)

# 	if answer == None:
# 		return False

# 	row = board.addToken(answer - 1, player.token)

# 	if row == -1 or row == None:
# 		return False

# 	strike = detectStrike(board, Vector(answer - 1, row), player.token)
# 	if strike != False:
# 		stopGame()
# 		interface.highlightedPoints = strike
# 		# interface.display_win()

# 	return True

# def onceUserPlayed(answer):
# 	row = board.addToken(answer - 1, USER.token)

# 	strike = detectStrike(board, Vector(answer - 1, row), USER.token)
# 	if strike != False:
# 		stopGame()
# 		interface.highlightedPoints = strike
# 		# interface.display_win()
	
# 	if playing:
# 		print("IA is playing")
# 		IA.play(board, onceIaPlayed)
	
# def onceIaPlayed(answer):
# 	row = board.addToken(answer - 1, IA.token)

# 	strike = detectStrike(board, Vector(answer - 1, row), IA.token)
# 	if strike != False:
# 		stopGame()
# 		interface.highlightedPoints = strike
# 		# interface.display_win()
	
# 	if playing:
# 		print("USER is playing")
# 		USER.play(board, onceUserPlayed)

# ==== Main loop ====

# USER.play(board, onceUserPlayed)

while playing:
	interface.renderScreen()

	# event treatment
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # quand la croix pour quitter est cliquée
			stopGame()

pygame.quit()