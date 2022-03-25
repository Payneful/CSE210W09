from asyncio import constants
from game.scripting.action import Action
from game.casting.ship import Ship
from game.casting.bullet import Bullet
from random import *
import random

import constants


class StageControl(Action):
    

    def __init__(self):
        self._stage = 0
        self.colors = [constants.BLUE, constants.GREEN, constants.YELLOW, constants.WHITE, constants.RED]

    def execute(self, cast, script):
        ships = cast.get_actors("ships")
    
        if not ships:
            if self._stage < constants.MAX_STAGE:
                self._stage = self._stage + 1
                self._setup(cast)
        
        else:
            self._ships_shoot(cast)


    def _setup(self, cast):
        for y in range(1, self._stage):
            for x in range(1, 40):
                cast.add_actor("ships", Ship((x + 20) * constants.CELL_SIZE, (y + 1) * constants.CELL_SIZE, self.colors[self._stage - 1]))

    def _ships_shoot(self, cast):
        dont_shoot_chance = 50 #Higher number = less chance to shoot
        shoot_chance = randint(1, dont_shoot_chance)
        if shoot_chance == 1: #shoot
            ships = cast.get_actors("ships")
            max_loop = 2 ** self._stage
            loop = randint(1, max_loop)
            for _ in range(1, loop):
                if len(ships) > 0:
                    ship = random.choice(ships)
                    cast.add_actor("bullets", Bullet(ship._position._x, ship._position._y + 15, "ship"))
                    ships.remove(ship) #Prevents a ship from being selected multiple times
                else:
                    break

