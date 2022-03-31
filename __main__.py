import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.ship import Ship
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.scripting.stage_control import StageControl
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.explosion_control import ExplosionControl
from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())

    level = constants.LEVELS
    key_name = "level_1"
    
    set_level_ships(level, key_name, cast)

    # cast.add_actor("ships", Ship())
    # cast.add_actor("ships", Ship(300))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    audio_service = AudioService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(audio_service))
    script.add_action("output", DrawActorsAction(video_service))

    script.add_action("update", StageControl())
    script.add_action("update", ExplosionControl())
    
    director = Director(video_service, audio_service)
    director.start_game(cast, script)


def set_level_ships(dictionary, key_name, cast):
    tokens = dictionary[key_name]
    ship_start = constants.SHIP_START

    for index_val in range(0, len(tokens)):
        token = tokens[index_val]
        if index_val < 20:
            pos = index_val * constants.CELL_SIZE + ship_start
            y_pos = 2 * constants.CELL_SIZE

        else:
            pos = (index_val % 20) * constants.CELL_SIZE + ship_start
            y_pos = (index_val // 20 + 2) *constants.CELL_SIZE
        


        if token == constants.X:
            cast.add_actor("ships", Ship(pos, y_pos))


if __name__ == "__main__":
    main()
    
    
    
# pyray.check_collision_boxes(box1: BoundingBox, box2: BoundingBox)