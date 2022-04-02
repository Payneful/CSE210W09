from game.casting.actor import Actor


class Lives(Actor):
    def __init__(self):
        super().__init__()
        self._lives = 3
        self.change_lives(0)
        self._position._y = 15

    def change_lives(self, lives):
        self._lives += lives
        self.set_text(f"Health: {self._lives}")

    def get_lives(self):
        return self._lives