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
        self.images = ["Ship1", "Ship2", "Ship3", "Ship4", "Ship5"]
        self._max_ships = constants.MAX_X // constants.CELL_SIZE - 10
        self._can_fire = False
        self._spawn_type = ["Default", "Crossing", "Edges", "Checkerd", "Downword"]

    def execute(self, cast, script):
        ships = cast.get_actors("ships")
    
        if not ships:
            # if self._stage < constants.MAX_STAGE:
            self._stage = self._stage + 1
            self._setup(cast)
        
        else:
            self._ships_shoot(cast, ships)


    def _setup(self, cast):
        formation = random.choice(self._spawn_type)
        alternater = 0
        for y in range(1, self._stage + 3):
            for x in range(1, self._max_ships):
                if formation == "Crossing": #Moves ships in from the sides alternating left and right by row 
                    if alternater % 2 == 0:
                        start_x = (((x - self._max_ships) - y) - 5) * constants.CELL_SIZE
                    else:
                        start_x = (((x + self._max_ships) + y) + 5 )* constants.CELL_SIZE
                    start_y = y * constants.CELL_SIZE
                
                elif formation == "Edges": #Splits the ships down the middle: right half comes from right edge, left half comes from left edge, middle comes from top. Ships overlap here
                    if x < ((constants.MAX_X // constants.CELL_SIZE)// 2) - 5:
                        start_x = -constants.CELL_SIZE
                        start_y = y * constants.CELL_SIZE
                    elif x == ((constants.MAX_X // constants.CELL_SIZE)// 2) - 5:
                        start_x = (x + 10) * constants.CELL_SIZE
                        start_y = -constants.CELL_SIZE
                    else:
                        start_x = constants.MAX_X + constants.CELL_SIZE
                        start_y = y * constants.CELL_SIZE
                
                elif formation == "Checkerd": #Moves ships in from the sides alternating each ship with overlapping.
                    if alternater % 2 == 0:
                        start_x = -constants.CELL_SIZE
                    else:
                        start_x = constants.MAX_X + constants.CELL_SIZE
                    start_y = y * constants.CELL_SIZE
                    alternater = alternater + 1
                
                elif formation == "Downword": #Moves ships down from the top of the screen into formation. Overlapping Y
                    start_x = (x + 10) * constants.CELL_SIZE
                    start_y = -constants.CELL_SIZE

                else: #Default Ships move down in one gathering in the middle into formation.
                    start_x = constants.MAX_X // 2
                    start_y = -constants.CELL_SIZE
                
                cast.add_actor("ships", Ship((x + 5) * constants.CELL_SIZE, (y + 1) * constants.CELL_SIZE, self.images[(self._stage - 1) % constants.MAX_STAGE], start_x, start_y))
            
            if formation == "Crossing":
                alternater = alternater + 1
            elif formation == "Checkerd":
                alternater = y

    def _ships_shoot(self, cast, ships):
        self._can_fire = True
        for ship in ships:
            if ship.advance == False:
                self._can_fire = False


        dont_shoot_chance = 50 #Higher number = less chance to shoot
        shoot_chance = randint(1, dont_shoot_chance)
        if shoot_chance == 1 and self._can_fire == True: #shoot
            max_loop = 10 ** self._stage
            loop = randint(1, max_loop)
            for _ in range(1, loop):
                if len(ships) > 0:
                    ship = random.choice(ships)
                    cast.add_actor("bullets", Bullet(ship._position._x, ship._position._y + 15, "ship"))
                    ships.remove(ship) #Prevents a ship from being selected multiple times
                else:
                    break

    