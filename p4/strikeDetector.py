from p4.board import Board
from p4.utils.vector import Vector
from p4.utils.token import Token

def detectStrike(board: Board, pos: Vector, token: Token):

	directions = [
		Vector(1, 1),
		Vector(0, 1),
		Vector(-1, 1),
		Vector(1, 0)
	]

	for direction in directions:
		result = is4Line(board, pos, direction, token)
		if result != False:
			return result
	
	return False

def is4Line(board: Board, pos: Vector, direction: Vector, token: Token):
	points = findLine(board, pos, direction, token)
	points.reverse()

	points.append(Vector(pos.c, pos.r))

	direction.multiply(-1)
	points += findLine(board, pos, direction, token)
	
	if len(points) >= 4:
		return points
	return False

def findLine(board: Board, pos: Vector, direction: Vector, token: Token):
	points = []

	pointer = Vector(pos.c, pos.r)
	pointer.add(direction)
	
	while (0 <= pointer.c < board.WIDTH
			and 0 <= pointer.r < board.HEIGHT
			and board.getColumn(pointer.c)[pointer.r] == token):

		points.append(Vector(pointer.c, pointer.r))

		pointer.add(direction)
	
	return points