from multiprocessing.sharedctypes import Value
from tkinter import N
from turtle import position
import constants
from game.casting.actor import Actor
from game.casting.explosion import Explosion
from game.scripting.action import Action
from game.shared.point import Point
# from game.services.audio_service import AudioService


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
        self._bullet_speed = constants.BULLET_SPEED
        self._points = constants.POINTS
        #self._hit = 

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_bullet_edge_of_map(cast)
            self._handle_ship_edge_collision(cast)
            self._handle_bullet_ship_collision(cast)
            # self._handle_game_over(cast)

    def _handle_bullet_edge_of_map(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        range = 10
        bullets = cast.get_actors("bullets")
        for bullet in bullets:
            if bullet._position.get_y() <= 0 or bullet._position.get_y() > constants.MAX_Y:
                cast.remove_actor("bullets", bullet)
    
    def _handle_ship_edge_collision(self, cast):
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

    def _handle_bullet_ship_collision(self, cast):
        """Determines if the bullet collides with the ships
        Args:
            self-- an instance of Handle_collisiions_action
            cast-- an instance of the cast class"""
        

        bullets = cast.get_actors("bullets")
        ships = cast.get_actors("ships")
        score = cast.get_first_actor("scores")
        player = cast.get_first_actor("snakes")


        for bullet in bullets:
            if bullet.ally != "ship":
                for ship in ships:
                    try:
                        if bullet._position.equals_range(ship._position, 10):
                            print("Enemy ship down!")
                            cast.add_actor("explosions", Explosion(ship._position.get_x(), ship._position.get_y()))
                            cast.remove_actor("bullets", bullet)
                            cast.remove_actor("ships", ship)
                            score.add_points(ship.score)
                    except(ValueError):
                        pass
            elif bullet.ally != "player":
                try:
                    if bullet._position.equals_range(player._position, 10):
                        print("Game Over")
                        cast.remove_actor("bullets", bullet)
                        cast.add_actor("explosions", Explosion(player._position.get_x(), player._position.get_y()))
                except(ValueError):
                    pass

    

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        