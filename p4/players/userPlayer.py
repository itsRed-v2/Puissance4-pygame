from typing import Callable
import pygame
from pygame.event import Event

from p4.players.player import Player
from p4.board import Board
from p4.display.interface import Interface

class UserPlayer(Player):
	def __init__(self, token, displayName, interface: Interface, addEventListener: Callable):
		self.interface = interface
		self.addEventListener = addEventListener
		super().__init__(token, displayName)

	def play(self, board: Board, playCB: Callable):
		def onMouseClick(event: Event):
			# do nothing if the event is not a left click (button 1)
			if event.button != 1:
				return False
			
			clickedCol = self.interface.getHoveredColumnIndex()
			# do nothing if click is not on a column
			if clickedCol == None:
				return False
			
			# do nothing if clicked column is full
			if board.getFirstEmpty(clickedCol) == -1:
				return False
			
			# calling the play callback
			playCB(clickedCol)
			return True # returning True removes this event listener from the main loop's event listeners

		self.addEventListener(pygame.MOUSEBUTTONUP, onMouseClick)
		