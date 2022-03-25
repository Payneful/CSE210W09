import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

        #added things
        self._firemode = 0

    def move_next(self):
        pass
        # # update velocities
        # previous = self._segments[0]
        # velocity = self._position()
        # # trailing.set_velocity(velocity)

    def turn_head(self, position):
        # self._position += int(position)
        self._position.add([position, 0])
    
    def _prepare_body(self):
        y = int(constants.CELL_SIZE * 55)
        x = int(constants.MAX_X / 2)
        self._position = Point(x, y)
        self._velocity = Point(0, 0)
        self._text = "#"
        self._color = constants.GREEN
        
    def firemode(self):
        """
        Attrabute to change firemode
        """
        pass