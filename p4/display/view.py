import pygame
from pygame import Color, Surface

from p4.players.player import Player
from p4.players.userPlayer import UserPlayer
from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token
from p4.display.interface import getHoveredColumn
from p4.constants import TOKEN_RADIUS, TOKEN_GAP, COLUMN_WIDTH, TOKEN_OUTLINE_WIDTH, TOKEN_COLORS, TOKEN_COLORS_HIGHLIGHT, BACKGROUND_COLOR

class View:
	def __init__(self, board: Board):
		self.board = board

		screenWidth = board.WIDTH * COLUMN_WIDTH + TOKEN_GAP
		screenHeight = board.HEIGHT * COLUMN_WIDTH + TOKEN_GAP
		self.screen = pygame.display.set_mode((screenWidth, screenHeight))

	def renderScreen(self, currentPlayer: Player | None):
		board = self.board
		screen = self.screen

		screen.fill(BACKGROUND_COLOR)
		
		# Drawing tokens
		for y in range(board.HEIGHT):
			for x in range(board.WIDTH):
				token = board.getTokenAt(x, y)
				color = TOKEN_COLORS[token]

				screenPos = getTokenScreenPos(x, y)
				
				pygame.draw.circle(screen, color, screenPos.asTuple(), TOKEN_RADIUS)

				if self.isHighlighted(x, y):
					assert token != Token.EMPTY

					outlineColor = TOKEN_COLORS_HIGHLIGHT[token]
					pygame.draw.circle(screen, outlineColor, screenPos.asTuple(), TOKEN_RADIUS + (TOKEN_OUTLINE_WIDTH / 2), width=TOKEN_OUTLINE_WIDTH)

		# Drawing hovered column
		if type(currentPlayer) == UserPlayer:
			hoveredCol = getHoveredColumn(board)
			if hoveredCol != None:
				rect = Surface((COLUMN_WIDTH, screen.get_height())) # initializing rectangle surface with right dimensions
				rect.fill(Color(255, 255, 255)) # setting color to white
				rect.set_alpha(20) # setting trensparency
				rectPos = (hoveredCol * COLUMN_WIDTH + (TOKEN_GAP / 2), 0) # coordinates at top left corner of the surface
				screen.blit(rect, rectPos) # blitting surface at right coordinates
				
		pygame.display.flip()
	
	def isHighlighted(self, x: int, y: int):
		for streak in self.board.streaks:
			for vec in streak:
				if vec.c == x and vec.r == y:
					return True
		return False

def getTokenScreenPos(boardX: int, boardY: int):
	pos = Vector(boardX, boardY)
	pos.multiply(COLUMN_WIDTH)
	offset = TOKEN_GAP + TOKEN_RADIUS
	pos.add(Vector(offset, offset))
	return pos