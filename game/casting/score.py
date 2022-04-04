from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, cast):
        super().__init__()
        self._points = 0
        self._reward = 0
        self._points_for_health = 10000
        self._lives = cast.get_first_actor("lives")
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        if self._points > self._points_for_health:
            self._points = self._points % self._points_for_health
            self._reward = self._reward + 1
            self._lives.change_lives(1)

        self.set_text(f"Score: {self._points + (self._points_for_health * self._reward)}")