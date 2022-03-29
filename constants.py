from tkinter.tix import CELL
from game.shared.color import Color
import pathlib

COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 50 * CELL_SIZE
MAX_Y = 60 * CELL_SIZE
FRAME_RATE = 20
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
POINTS = 100
BULLET_SPEED = 1

SHIP_SCORE = 1


ROOT_PATH = pathlib.Path(__file__).parent.resolve().parent.resolve()


# BOUNCE_SOUND = str(ROOT_PATH.joinpath("batter/assets/sounds/boing.wav"))