from tkinter import N
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            self._handle_time_change(cast)
            
    def _handle_time_change(self,cast):
        """Per frame changing for the worm growth.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        for snake in snakes:
            snake.grow_tail(1)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        heads = []
        segments = []
        for snake in snakes:
            heads.append(snake.get_segments()[0])
            segments.append(snake.get_segments()[1:])

        # for i in range(0, len(heads) -1):
        #     for segment in segments:
        #         if heads[i].get_position().equals(segment.get_position()):
        #             #snake = dead
        #             heads.pop(i)
        #             if len(heads) == 1:
        #                 self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snakes = cast.get_actors("snakes")
            snake1 = snakes[0]
            snake2 = snakes[1]
            segments = snake1.get_segments() + snake2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            text = f"Game Over!\nPlayer {self._winner} wins!"
            message = Actor()
            message.set_text(text)
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)