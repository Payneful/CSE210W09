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
        # update velocities
        previous = self._segments[0]
        velocity = previous.get_velocity()
        trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def turn_head(self, position):
        self._segments[0].add_position(position)
    
    def _prepare_body(self):
        y = int(constants.CELL_SIZE * 2)
        x = int(constants.MAX_X / 2)
        position = Point(x, y * constants.CELL_SIZE)
        velocity = Point(0, 0)
        text = "#"
        color = constants.GREEN
            
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)


    def firemode(self):
        """
        Attrabute to change firemode
        """
        pass

    def shoot(self):
        """
        Attrabute to shoot projectiles
        """
        pass