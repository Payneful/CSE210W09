from tkinter import N
from turtle import position
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
            self._handle_bullet_collision(cast)
            self._handle_edge_collision(cast)
            # self._handle_game_over(cast)

    def _handle_bullet_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        range = 10
        bullets = cast.get_actors("bullets")
        for bullet in bullets:
            if bullet._position.get_y() <= 0 or bullet._position.get_y() >= constants.MAX_Y:
                cast.remove_actor("bullets", bullet)
            elif bullet.ally != "ship": #collision with ships
                ships = cast.get_actors("ships") 
                for ship in ships:
                    if ship._position.get_x() + range >= bullet._position.get_x() and ship._position.get_y() + range >= bullet._position.get_y() and ship._position.get_x() - range <= bullet._position.get_x() and ship._position.get_y() - range <= bullet._position.get_y():
                        cast.remove_actor("ships", ship)
                        cast.remove_actor("bullets", bullet)
                        break
            elif bullet.ally != "player":
                player = cast.get_first_actor("snakes")
                if player._position.get_x() + range >= bullet._position.get_x() and player._position.get_y() + range >= bullet._position.get_y() and player._position.get_x() - range <= bullet._position.get_x() and player._position.get_y() - range <= bullet._position.get_y():
                    print("Game Over")
                    cast.remove_actor("bullets", bullet)
                    break
                    




    
    def _handle_edge_collision(self, cast):
        """
        Reverses movment of ships when they hit the edge of the screen"""
        change_direction = False
        ships = cast.get_actors("ships")

        for ship in ships:
            if ship._position._x <= 1 * constants.CELL_SIZE and ship.direction < 0 or ship._position._x >= constants.MAX_X - constants.CELL_SIZE and ship.direction > 0: #if the ship is on left edge and moving left or on right edge moving right
                change_direction = True
                break
        if change_direction == True:
            for ship in ships:
                ship.direction = ship.direction * -1
                ship._position.add([0, 15])

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