import pygame

from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token

TOKEN_RADIUS = 50 # radius of a token on the screen
TOKEN_GAP = 25 # gap between 2 tokens vertically and horizontally
COLUMN_WIDTH = TOKEN_RADIUS * 2 + TOKEN_GAP

TOKEN_COLORS = {
	Token.BLUE: (0, 182, 207),
	Token.YELLOW: (252, 252, 0),
	Token.EMPTY: (220, 220, 220)
}

class Interface:
	def __init__(self, board: Board):
		self.board = board
		self.highlightedPoints = []

		screenHeight = board.HEIGHT * COLUMN_WIDTH + TOKEN_GAP
		screenWidth = board.WIDTH * COLUMN_WIDTH + TOKEN_GAP
		self.screen = pygame.display.set_mode((screenWidth, screenHeight))

	def renderScreen(self):
		board = self.board
		screen = self.screen

		screen.fill((200, 200, 200))
		
		# Drawing tokens
		for y in range(board.HEIGHT):
			for x in range(board.WIDTH):
				column = board.getColumn(x)
				assert column != None
				token = column[y]
				color = TOKEN_COLORS[token]

				pos = Vector(x, y)
				pos.multiply(COLUMN_WIDTH)
				offset = TOKEN_GAP + TOKEN_RADIUS
				pos.add(Vector(offset, offset))
				
				pygame.draw.circle(screen, color, pos.asTuple(), TOKEN_RADIUS)

		# Drawing hovered column
		hoveredCol = self.getHoveredColumnIndex()
		if hoveredCol != None:
			rect = pygame.Surface((COLUMN_WIDTH, screen.get_height())) # initializing rectangle surface with right dimensions
			rect.fill(pygame.Color(255, 255, 255)) # setting color to white
			rect.set_alpha(50) # setting trensparency
			rectPos = (hoveredCol * COLUMN_WIDTH + (TOKEN_GAP / 2), 0) # coordinates at top left corner of the surface
			screen.blit(rect, rectPos) # blitting surface at right coordinates
				
		pygame.display.flip()
	
	def getHoveredColumnIndex(self):
		if not pygame.mouse.get_focused(): # if mouse is out of the game window
			return None

		mousePos = pygame.mouse.get_pos()
		mouseX = mousePos[0]
		hoveredColIndex = int((mouseX - TOKEN_GAP/2) // COLUMN_WIDTH) # calculating the index of the column hovered by the mouse (first col is 0, etc..)
		if hoveredColIndex < 0 or hoveredColIndex >= self.board.WIDTH: # if hovered column is outside of the board
			return None
		return hoveredColIndex