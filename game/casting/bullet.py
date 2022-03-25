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
