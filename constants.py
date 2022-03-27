from game.shared.color import Color


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 1200
MAX_Y = 900
FRAME_RATE = 12
FONT_SIZE = 15
CAPTION = "Snake"
SNAKE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(255, 0, 255)

POINTS = 100
BULLET_SPEED = 1

# X represents ship locations. O represents empty spaces.
X = "X"
O = "O"
LEVELS = {"level_1":[X, X, X, O, O, X, X, O, O, O, X, X, O, O, O, X, X, O, O, X,
                     X, X, O, O, X, X, X, O, O, X, X, X, X, O, O, X, X, X, X, O, 
                     X, X, X, X, O, X, X, O, O, O, O, O, X, X, X, O, O, X, X, X, 
                     ]
        }

SHIP_START = 450