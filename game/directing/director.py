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