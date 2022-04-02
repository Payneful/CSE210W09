class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service, audio_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._audio_service = audio_service

        self._audio_service.initialize()
        self._audio_service.load_sounds("Game/Assets/Sounds/boing.wav", "Boing")

        
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        self._video_service.load_image("Game\Assets\Images\Player.png", "Player", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Player_lazer.png", "Player Lazer", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Ship_lazer.png", "Ship Lazer", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Alien_blue.png", "Ship1", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Alien_green.png", "Ship2", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Alien_orange.png", "Ship3", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Alien_red.png", "Ship4", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Alien_purple.png", "Ship5", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion1.png", "Explosion1", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion2.png", "Explosion2", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion3.png", "Explosion3", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion4.png", "Explosion4", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion5.png", "Explosion5", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion6.png", "Explosion6", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion7.png", "Explosion7", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion8.png", "Explosion8", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion9.png", "Explosion9", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion10.png", "Explosion10", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion11.png", "Explosion11", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion12.png", "Explosion12", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion13.png", "Explosion13", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion14.png", "Explosion14", 0, 0, 0)
        self._video_service.load_image("Game\Assets\Images\Explosion15.png", "Explosion15", 0, 0, 0)
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast, script)