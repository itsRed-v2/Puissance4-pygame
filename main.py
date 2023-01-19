import sys
import pygame
from typing import Callable

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
# ==================

interface = Interface(board)

playing = True

def stopGame():
	global playing
	playing = False

# Event listening things
# TODO: replace this with more specific stuff because this is uselessly over engineered

class EventListener():
	def __init__(self, eventType, onEvent: Callable):
		self.type = eventType
		self.onEvent = onEvent

eventListeners: list[EventListener] = []

def listenForEvent(eventType, onEvent: Callable):
	eventListeners.append(EventListener(eventType, onEvent))

def processListeners(event: pygame.event.Event):
	for listener in eventListeners:
		if listener.type == event.type:
			isRemoved = listener.onEvent(event)
			if isRemoved:
				eventListeners.remove(listener)

# Players initialization

USER = UserPlayer(Token.YELLOW, Color.YELLOW + "Utilisateur", interface, listenForEvent)
IA = IAPlayer(Token.BLUE, Color.BLUE + "Ordi")

# Players playing functions

def processAction(colIndex, player):
	row = board.addToken(colIndex, player.token)
	assert row != -1 and row != None

	strike = detectStrike(board, Vector(colIndex, row), player.token)
	if strike != False:
		stopGame()
		interface.highlightedPoints = strike
		# interface.display_win()

def onceUserPlayed(answer):
	processAction(answer, USER)
	
	if playing:
		print("IA is playing")
		IA.play(board, onceIaPlayed)
	
def onceIaPlayed(answer):
	processAction(answer, IA)
	
	if playing:
		print("USER is playing")
		USER.play(board, onceUserPlayed)

# ==== Main loop ====

USER.play(board, onceUserPlayed)

def mainLoop():
	while True:
		interface.renderScreen()

		# event treatment
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # quand la croix pour quitter est cliquée
				stopGame()
				return
			
			processListeners(event)

mainLoop()

pygame.quit()