import sys

from p4.players.IAplayer import IAPlayer
from p4.players.userPlayer import UserPlayer

from p4.board import Board
from p4.utils.token import Token
from p4.utils.vector import Vector
from p4.utils.color import Color

from p4.display.gameView import View

from p4.strikeDetector import detectStrike

board = Board()

# Custom sized board
if len(sys.argv) == 3:
	h = sys.argv[1]
	w = sys.argv[2]
	
	if h.isdecimal() and w.isdecimal():
		board = Board(height = int(h), width = int(w))
# ==

view = View(board)

playing = True

def stopGame():
	global playing
	playing = False

USER = UserPlayer(Token.YELLOW, Color.YELLOW + "Utilisateur", view, stopGame)
IA = IAPlayer(Token.BLUE, Color.BLUE + "Ordi")

def play(player):
	answer = player.play(board)

	if answer == None:
		return False

	row = board.addToken(answer - 1, player.token)

	if row == -1 or row == None:
		return False

	strike = detectStrike(board, Vector(answer - 1, row), player.token)
	if strike != False:
		stopGame()
		view.highlightedPoints = strike
		view.display_win(player.displayName)

	return True

# ==== Main loop ====

while playing:

	view.displayGame(USER.displayName)
	play(USER)

	if not playing: break

	view.displayGame(IA.displayName)
	if not play(IA):
		print(Color.RED + "AI played wrong!!")
		playing = False