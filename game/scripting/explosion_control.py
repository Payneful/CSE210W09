from game.scripting.action import Action
import constants


class ExplosionControl(Action):
    def execute(self, cast, script):
        explosions = cast.get_actors("explosions")
        for explosion in explosions:
            if explosion.stage < constants.FRAME_RATE:
                explosion.progress()
                explosion.stage = explosion.stage + 1 
            else:
                cast.remove_actor("explosions", explosion)
