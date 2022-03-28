import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Bullet(Actor):
    """
    Projectile to destroy targets
    """

    def __init__(self, position_x, position_y, ally = "player"):
        super().__init__()
        self._prepare_bullet(position_x + 4, position_y, ally)
        self._set_velocity()
        
    def _set_velocity(self):
        if self.ally == "player":
            self._velocity = Point(0, -15)
            self._color = constants.BLUE
        else:
            self._velocity = Point(0, 15)
            self._color = constants.RED

    def _prepare_bullet(self, position_x, position_y, ally):
        self.ally = ally
        self._position = Point(position_x, position_y)
        self._text = "|"

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        for _ in range(constants.BULLET_SPEED):
            x = (self._position.get_x() + self._velocity.get_x())
            y = (self._position.get_y() + self._velocity.get_y())
            self._position = Point(x, y)
