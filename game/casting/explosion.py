import constants
import math
from game.casting.actor import Actor
from game.shared.point import Point


class Explosion(Actor):
    
    def __init__(self, x, y):
        super().__init__()
        self.stage = 0
        self._position = Point(x, y)
        self._text = "O"
        self._colors = [constants.RED, constants.YELLOW]

    def progress(self):
        self._color = self._colors[self.stage % 2]

