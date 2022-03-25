from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def _adjust_ship_speed(self, cast):
        ships = cast.get_actors("ships")

        for ship in ships:
            ship.speed = 15 / (len(ships)/2)

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._adjust_ship_speed(cast)

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()