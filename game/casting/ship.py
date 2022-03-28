
from re import X
from tkinter import Y
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Ship(Actor):
    """
    Enemy object.
    Starts at the top and slowly snakes their way down to the bottom of the screen as a unit not individualy
    Occationaly shoots at player
    Win by destroying all of them loose if they shoot or reach player
    """

    def __init__(self, x = int(constants.MAX_X / 2), y = 2 * constants.CELL_SIZE, color = constants.BLUE, start_x = 0, start_y = 0):
        """
        Parameters: x position, y position,  
        """
        super().__init__()
        self._position = Point(x, y)
        self.direction = 1 #1 is Right, -1 is Left. This also operates as a speed multiplier and can take floats without breaking anything.
        self._velocity = Point(0, 0) #starts off going Right
        self._color = color
        self._text = "V"
        self.speed = 1
        self._starting_y = y
        self.score = 1000

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        self._velocity._x = int((self.speed * self.direction))
        x = (self._position.get_x() + self._velocity.get_x())# % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y())# % constants.MAX_Y
        self._position = Point(x, y)

        self.score = int(constants.SHIP_SCORE * (constants.MAX_Y - self._position.get_y()) / constants.CELL_SIZE)
        
