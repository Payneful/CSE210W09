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

    # def __init__(self, keyboard_service):
    #     """Constructs a new ControlActorsAction using the specified KeyboardService.
        
    #     Args:
    #         keyboard_service (KeyboardService): An instance of KeyboardService.
    #     """
    #     self._keyboard_service = keyboard_service
    #     self._direction = Point(constants.CELL_SIZE, 0)

    # def execute(self, cast, script):
    #     """Executes the control actors action.

    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #         script (Script): The script of Actions in the game.
    #     """
    #     snakes = cast.get_actors("snakes")

    #     # left
    #     if self._keyboard_service.is_key_down('a'):
    #         snakes[0].turn_head(Point(-constants.CELL_SIZE, 0))
        
    #     # right
    #     if self._keyboard_service.is_key_down('d'):
    #         snakes[0].turn_head(Point(constants.CELL_SIZE, 0))
        
    #     # up
    #     if self._keyboard_service.is_key_down('w'):
    #         snakes[0].turn_head(Point(0, -constants.CELL_SIZE))
        
    #     # down
    #     if self._keyboard_service.is_key_down('s'):
    #         snakes[0].turn_head(Point(0, constants.CELL_SIZE))
        
    #     # left
    #     if self._keyboard_service.is_key_down('j'):
    #         snakes[1].turn_head(Point(-constants.CELL_SIZE, 0))
            
    #     # right
    #     if self._keyboard_service.is_key_down('l'):
    #         snakes[1].turn_head(Point(constants.CELL_SIZE, 0))
        
    #     # up
    #     if self._keyboard_service.is_key_down('i'):
    #         snakes[1].turn_head(Point(0, -constants.CELL_SIZE))
        
    #     # down
    #     if self._keyboard_service.is_key_down('k'):
    #         snakes[1].turn_head(Point(0, constants.CELL_SIZE))
        

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self.key1 = 's'
        self.key2 = 'k'
        self.key3 = 'KEY_DOWN'
        self.player1_move = ["a", "s", "w", "d"]
        self.player2_move = ["j", "k", "l", "i"]

        
    def execute(self, cast, script):
        """Executes the control actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        snakes = cast.get_actors("snakes")
        # left
        if self._keyboard_service.is_key_down('a'):
            if self._validate_direction('a'):
                snakes[0].turn_head(Point(-constants.CELL_SIZE, 0))
                self.key1 = "a"
        
        # right
        if self._keyboard_service.is_key_down('d'):
            if self._validate_direction('d'):
                snakes[0].turn_head(Point(constants.CELL_SIZE, 0))
                self.key1 = "d"
        
        # up
        if self._keyboard_service.is_key_down('w'):
            if self._validate_direction('w'):
                snakes[0].turn_head(Point(0, -constants.CELL_SIZE))
                self.key1 = "w"
        
        # down
        if self._keyboard_service.is_key_down('s'):
            if self._validate_direction('s'):
                snakes[0].turn_head(Point(0, constants.CELL_SIZE))
                self.key1 = "s"
        
        # left
        if self._keyboard_service.is_key_down('j'):
            if self._validate_direction('j'):
                snakes[1].turn_head(Point(-constants.CELL_SIZE, 0))
                self.key2 = "j"
        # right
        if self._keyboard_service.is_key_down('l'):
            if self._validate_direction('l'):
                snakes[1].turn_head(Point(constants.CELL_SIZE, 0))
                self.key2 = "l"
        
        # up
        if self._keyboard_service.is_key_down('i'):
            if self._validate_direction('i'):
                snakes[1].turn_head(Point(0, -constants.CELL_SIZE))
                self.key2 = "i"
        
        # down
        if self._keyboard_service.is_key_down('k'):
            if self._validate_direction('k'):
                snakes[1].turn_head(Point(0, constants.CELL_SIZE))
                self.key2 = "k"
        
            
    def _validate_direction(self, key_pressed):
        """Validiates user input to prevent user from moving back on
        themselves: If the user is going left, then they should not
        imediately move right.
        Args:
            self-- an instance of Control_actors
            key_pressed-- the users key pressed"""
        
        # directions for snake[0]
        if key_pressed in self.player1_move:
            left = "a"
            opposite_left = "d"

            opposite_down = "w"
            down = "s"

            opposite_up = "s"
            up = "w"

            opposite_right = "a"
            right = "d"

            last_direction = self.key1

        # directions for snake[1]
        elif key_pressed in self.player2_move:
            left = "j"
            opposite_left = "l"

            opposite_down = "i"
            down = "k"

            opposite_up = "k"
            up = "i"

            opposite_right = "j"
            right = "l"

            last_direction = self.key2

        # Validate movement
        valid_move = True
        if key_pressed == left:
            if last_direction == opposite_left:
                valid_move = False
        
        elif key_pressed == right:
            if last_direction == opposite_right:
                valid_move = False

        elif key_pressed == down:
            if last_direction == opposite_down:
                valid_move = False

        elif key_pressed == up:
            if last_direction == opposite_up:
                valid_move = False
        
        return valid_move