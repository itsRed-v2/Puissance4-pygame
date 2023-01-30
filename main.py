import sys
import pygame

from p4.players.player import Player
from p4.players.IAplayer import IAPlayer
from p4.players.userPlayer import UserPlayer

from p4.board import Board
from p4.utils.token import Token
from p4.utils.color import Color

from p4.display.view import View

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Puissance 4")

board = Board()

# Custom sized board
if len(sys.argv) == 3:
	h = sys.argv[1]
	w = sys.argv[2]
	
	if h.isdecimal() and w.isdecimal():
		board = Board(height = int(h), width = int(w))
# ==================

view = View(board)

playing = True

def stopGame():
	global playing
	playing = False

# Players initialization

USER = UserPlayer(Token.YELLOW, Color.YELLOW + "Utilisateur")
IA = IAPlayer(Token.BLUE, Color.BLUE + "Ordi")

currentPlayer = USER

# Records player's decision and checks if he won
def processAction(colIndex, player: Player):
	board.addToken(colIndex, player.token)

	if len(board.streaks) > 0: # if the player just won
		stopGame()
		global currentPlayer
		currentPlayer = None

# This callback function is called by players when they chose their answer
def oncePlayed(answer):
	global currentPlayer
	assert currentPlayer != None
	processAction(answer, currentPlayer)

	if playing: # playing may be false if the game ended after processAction() was called
		# Swapping current player
		if currentPlayer == USER:
			currentPlayer = IA
		else: currentPlayer = USER

		# asking new current player to play
		currentPlayer.play(board, oncePlayed)

# asking the first player to play the first round
currentPlayer.play(board, oncePlayed)

# ==== Main loop ====

def mainLoop():
	while True:
		view.renderScreen(currentPlayer)

		# event treatment
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # quand la croix pour quitter est cliquée
				stopGame()
				return
			
			if event.type == pygame.MOUSEBUTTONUP and currentPlayer == USER:
				USER.onMouseClick(event)
				
		IA.tick()

		clock.tick(60)
			
mainLoop()

pygame.quit()