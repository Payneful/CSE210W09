from game.casting.actor import Actor

class Text(Actor):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._font_size = 32