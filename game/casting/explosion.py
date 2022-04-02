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
        self._images = ["Explosion1", "Explosion2", "Explosion3", "Explosion4", "Explosion5", "Explosion6", "Explosion7", "Explosion8", "Explosion9", "Explosion10", "Explosion11", "Explosion12", "Explosion13", "Explosion14", "Explosion15"]

    def progress(self):
        self._image = self._images[self.stage % 16]

