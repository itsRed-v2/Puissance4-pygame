from typing import Callable
from pygame.event import Event

from p4.players.player import Player
from p4.board import Board
from p4.display.interface import getHoveredColumn

class UserPlayer(Player):
	def __init__(self, token, displayName):
		self.onMouseClick: Callable[[Event], None]
		self.setMouseEventPassive()
		super().__init__(token, displayName)

	def setMouseEventPassive(self):
		def passiveMethod(event: Event):
			pass
		self.onMouseClick = passiveMethod

	def play(self, board: Board, playCB: Callable):
		def onMouseClick(event: Event):
			# do nothing if the event is not a left click (button 1)
			if event.button != 1:
				return
			
			clickedCol = getHoveredColumn(board)
			# do nothing if click is not on a column
			if clickedCol == None:
				return
			
			# do nothing if clicked column is full
			if board.getFirstEmpty(clickedCol) == -1:
				return
			
			# making the mouseEvent processor passive again
			self.setMouseEventPassive()
			# calling the play callback
			playCB(clickedCol)

		self.onMouseClick = onMouseClick
		