from pygame import Color
from p4.utils.token import Token

TOKEN_RADIUS = 50 # radius of a token on the screen
TOKEN_GAP = 25 # gap between 2 tokens vertically and horizontally
COLUMN_WIDTH = TOKEN_RADIUS * 2 + TOKEN_GAP
TOKEN_OUTLINE_WIDTH = 10

BACKGROUND_COLOR = Color(54, 70, 82)
TOKEN_COLORS = {
	Token.BLUE: Color(89, 165, 216),
	Token.YELLOW: Color(255, 192, 92),
	Token.EMPTY: Color(64, 84, 99)
}

TOKEN_COLORS_HIGHLIGHT = {
	Token.BLUE: Color(35, 103, 149),
	Token.YELLOW: Color(224, 138, 0),
}