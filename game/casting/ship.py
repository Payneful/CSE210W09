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

    def __init__(self, x = int(constants.MAX_X / 2), y = 2 * constants.CELL_SIZE, color = constants.BLUE):
        """
        Parameters: x position, y position,  
        """
        pass
        super().__init__()
        self._position = Point(x, y)
        self._velocity = Point(15, 0) #starts off going Right
        self._color = color
        self._text = "V"


    def _shoot(self):
        pass
