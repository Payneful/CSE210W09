from tkinter.tix import CELL
from game.shared.color import Color
import pathlib

COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 40 * CELL_SIZE #Subtract this with 10 to get Max ship count. Max_X // CELL_SIZE - 10
MAX_Y = 60 * CELL_SIZE
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
BLACK = Color(0, 0, 0)

MAX_STAGE = 5
MAX_SHIP_SPEED = 5
BULLET_SPEED = 1

SHIP_SCORE = 1

#0 = empty, 1 is blue, 2 is Green, 3 is Orange, 4 is Red, and 5 is Purple

LEVELS = {0:    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }

