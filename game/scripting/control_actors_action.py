import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.bullet import Bullet


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """  

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self.key3 = 'KEY_DOWN'
        self.player1_move = ["a", "d", "space"]

        
    def execute(self, cast, script):
        """Executes the control actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        snake = cast.get_first_actor("snakes")

        # left
        if self._keyboard_service.is_key_down('a'):
            snake.turn_head(-constants.CELL_SIZE)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            snake.turn_head(constants.CELL_SIZE)

        # stop
        # if not self._keyboard_service.is_key_down('a') and not self._keyboard_service.is_key_down('d'):
        #     print(Point(0,0))
        #     print(type(Point(0,0)))
        #     snake.turn_head(Point(0, 0))
            
        # firemode
        # if self._keyboard_service.is_key_down('f'):
        #     snake.fireMode()
        
        # shoot
        if self._keyboard_service.is_key_down('spacebar'):
            cast.add_actor("bullets", Bullet(snake._position.get_x(),snake._position.get_y()))
