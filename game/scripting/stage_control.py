from asyncio import constants
from game.scripting.action import Action
from game.casting.ship import Ship
import constants


class StageControl(Action):
    

    def __init__(self):
        self._stage = 0
        self.colors = [constants.BLUE, constants.GREEN, constants.YELLOW, constants.WHITE, constants.RED]

    def execute(self, cast, script):
        ships = cast.get_actors("ships")
        if not ships and self._stage < constants.MAX_STAGE:
            self._stage = self._stage + 1
            self._setup(cast)


    def _setup(self, cast):
        for y in range(1, self._stage):
            for x in range(1, 21):
                cast.add_actor("ships", Ship((x + 20) * constants.CELL_SIZE, (y + 1) * constants.CELL_SIZE, self.colors[self._stage - 1]))
