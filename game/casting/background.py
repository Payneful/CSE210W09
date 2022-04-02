from game.casting.actor import Actor


class Background(Actor):
    
    def __init__(self):
        super().__init__()
        self._image = "background"