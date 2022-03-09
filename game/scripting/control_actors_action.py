import constants
from game.scripting.action import Action
from game.shared.point import Point


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

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snakes = cast.get_actors("snakes")

        # left
        if self._keyboard_service.is_key_down('a'):
            snakes[0].turn_head(Point(-constants.CELL_SIZE, 0))
        
        # right
        if self._keyboard_service.is_key_down('d'):
            snakes[0].turn_head(Point(constants.CELL_SIZE, 0))
        
        # up
        if self._keyboard_service.is_key_down('w'):
            snakes[0].turn_head(Point(0, -constants.CELL_SIZE))
        
        # down
        if self._keyboard_service.is_key_down('s'):
            snakes[0].turn_head(Point(0, constants.CELL_SIZE))
        
        # left
        if self._keyboard_service.is_key_down('j'):
            snakes[1].turn_head(Point(-constants.CELL_SIZE, 0))
            
        # right
        if self._keyboard_service.is_key_down('l'):
            snakes[1].turn_head(Point(constants.CELL_SIZE, 0))
        
        # up
        if self._keyboard_service.is_key_down('i'):
            snakes[1].turn_head(Point(0, -constants.CELL_SIZE))
        
        # down
        if self._keyboard_service.is_key_down('k'):
            snakes[1].turn_head(Point(0, constants.CELL_SIZE))
        
        """
        snake = cast.get_actors("snakes")
        if worm1:
            snake[0].turn_head(self._direction)

        if worm2:
            snake[1].turn_head(self._direction)
        """