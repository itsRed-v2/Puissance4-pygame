import pygame
from pygame import Color, Surface

from p4.players.player import Player
from p4.players.userPlayer import UserPlayer
from p4.board import Board
from p4.utils.vector import Vector
from p4.display.interface import getHoveredColumn
from p4.constants import TOKEN_RADIUS, TOKEN_GAP, COLUMN_WIDTH, TOKEN_COLORS

class View:
	def __init__(self, board: Board):
		self.board = board
		self.highlightedPoints = []

		screenHeight = board.HEIGHT * COLUMN_WIDTH + TOKEN_GAP
		screenWidth = board.WIDTH * COLUMN_WIDTH + TOKEN_GAP
		self.screen = pygame.display.set_mode((screenWidth, screenHeight))

	def renderScreen(self, currentPlayer: Player | None):
		board = self.board
		screen = self.screen

		screen.fill(Color(200, 200, 200))
		
		# Drawing tokens
		for y in range(board.HEIGHT):
			for x in range(board.WIDTH):
				token = board.getTokenAt(x, y)
				color = TOKEN_COLORS[token]

				pos = Vector(x, y)
				pos.multiply(COLUMN_WIDTH)
				offset = TOKEN_GAP + TOKEN_RADIUS
				pos.add(Vector(offset, offset))
				
				pygame.draw.circle(screen, color, pos.asTuple(), TOKEN_RADIUS)

		# Drawing hovered column
		if type(currentPlayer) == UserPlayer:
			hoveredCol = getHoveredColumn(board)
			if hoveredCol != None:
				rect = Surface((COLUMN_WIDTH, screen.get_height())) # initializing rectangle surface with right dimensions
				rect.fill(Color(255, 255, 255)) # setting color to white
				rect.set_alpha(50) # setting trensparency
				rectPos = (hoveredCol * COLUMN_WIDTH + (TOKEN_GAP / 2), 0) # coordinates at top left corner of the surface
				screen.blit(rect, rectPos) # blitting surface at right coordinates
				
		pygame.display.flip()