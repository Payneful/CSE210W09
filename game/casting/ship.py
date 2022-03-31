
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

    def __init__(self, x = int(constants.MAX_X / 2), y = 2 * constants.CELL_SIZE, image = "Ship1", start_x = constants.MAX_X // 2, start_y = -15):
        """
        Parameters: x position, y position,  
        """
        super().__init__()
        self._position = Point(start_x, start_y)
        self.direction = 1 #1 is Right, -1 is Left. This also operates as a speed multiplier and can take floats without breaking anything.
        self._velocity = Point(0, 0) #starts off going Right
        self._text = "V"
        self.speed = 1
        self.score = constants.SHIP_SCORE
        self._x = x 
        self._y = y
        self.advance = False
        self.ready_to_advance = False
        self._formation_speed = 5
        self._image = image
        self.shield = 3

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        if self.advance:
            self._velocity._x = int((self.speed * self.direction))

        else:
            self.speed = self.speed * self._formation_speed
            if self._position.get_x() > self._x + self.speed:
                self._velocity._x = -self.speed
            elif self._position.get_x() < self._x - self.speed:
                self._velocity._x = self.speed
            else:
                self._velocity._x = 0
                self._position._x = self._x
            
            if self._position.get_y() > self._y + self.speed:
                self._velocity._y = -self.speed
            elif self._position.get_y() < self._y - self.speed:
                self._velocity._y = self.speed
            else:
                self._velocity._y = 0
                self._position._y = self._y

            if self._velocity.get_x() == 0 and self._velocity.get_y() == 0:
                self.ready_to_advance = True

        
        x = int((self._position.get_x() + self._velocity.get_x()))# % constants.MAX_X
        y = int((self._position.get_y() + self._velocity.get_y()))# % constants.MAX_Y
        self._position = Point(x, y)
        self.score = int(constants.SHIP_SCORE * (constants.MAX_Y - self._position.get_y()) / constants.CELL_SIZE)

            
