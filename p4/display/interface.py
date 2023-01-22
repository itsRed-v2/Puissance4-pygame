from pygame import mouse

from p4.constants import TOKEN_GAP, COLUMN_WIDTH

def getHoveredColumn(board):
	if not mouse.get_focused(): # if mouse is out of the game window
		return None

	mousePos = mouse.get_pos()
	mouseX = mousePos[0]
	hoveredColIndex = int((mouseX - TOKEN_GAP/2) // COLUMN_WIDTH) # calculating the index of the column hovered by the mouse (first col is 0, etc..)
	if hoveredColIndex < 0 or hoveredColIndex >= board.WIDTH: # if hovered column is outside of the board
		return None
	return hoveredColIndex