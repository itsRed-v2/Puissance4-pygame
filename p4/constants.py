from pygame import Color
from p4.utils.token import Token

TOKEN_RADIUS = 50 # radius of a token on the screen
TOKEN_GAP = 25 # gap between 2 tokens vertically and horizontally
COLUMN_WIDTH = TOKEN_RADIUS * 2 + TOKEN_GAP

TOKEN_COLORS = {
	Token.BLUE: Color(0, 182, 207),
	Token.YELLOW: Color(252, 252, 0),
	Token.EMPTY: Color(220, 220, 220)
}