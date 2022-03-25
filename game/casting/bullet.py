import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Bullet(Actor):
    """
    Projectile to destroy targets
    """

    def __init__(self, position_x, position_y, ally = "player"):
        super().__init__()
        self._prepare_bullet(position_x, position_y, ally)
        
    def _set_velocity(self):
        if self._ally == "player":
            self._set_velocity(0, -15)
            self.color = constants.BLUE
        else:
            self._set_velocity(0, 15)
            self.color = constants.RED

    def _prepare_bullet(self, position_x, position_y, ally):
        self._ally = ally
        self._position = Point(position_x, position_y)
        self._velocity = Point(0, 0)
        self._text = "^"
        self.color = constants.WHITE
