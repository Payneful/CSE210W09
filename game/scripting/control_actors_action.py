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
        self.key1 = 'w'
        self.key2 = 'i'
        self.key3 = 'UP_KEY'
        
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
        
        # left
        if self._keyboard_service.is_key_down('KEY_LEFT'):
            snakes[2].turn_head(Point(-constants.CELL_SIZE, 0))
            
        # right
        if self._keyboard_service.is_key_down('KEY_RIGHT'):
            snakes[2].turn_head(Point(constants.CELL_SIZE, 0))
        
        # up
        if self._keyboard_service.is_key_down('KEY_UP'):
            snakes[2].turn_head(Point(0, -constants.CELL_SIZE))
        
        # down
        if self._keyboard_service.is_key_down('KEY_DOWN'):
            snakes[2].turn_head(Point(0, constants.CELL_SIZE))
            
    def _validate_direction(self, key_pressed):
        """Validiates user input to prevent user from moving back on
        themselves: If the user is going left, then they should not
        imediately move right.
        Args:
            self-- an instance of Control_actors
            key_pressed-- the users key pressed"""
        
        # Opposites for snake[0]
        opposite_a = "d"
        opposite_s = "w"
        opposite_w = "s"
        opposite_d = "a"

        # Opposites for snake[1]
        opposite_i = "k"
        opposite_j= "l"
        opposite_k = "i"
        opposite_l = "j"

        # Opposites for snake[2]
        opposite_key_up = "KEY_DOWN"
        opposite_key_left = "KEY_RIGHT"
        opposite_key_right = "KEY_LEFT"
        opposite_key_down = "KEY_UP"

        # snake[0] validation 
        if key_pressed == "d":
            pass

        elif key_pressed == "w":
            pass

        elif key_pressed == "s":
            pass

        elif key_pressed == "a":
            pass

        # snake[1] validiation
