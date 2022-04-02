from game.scripting.action import Action
import constants

class MusicControl(Action):
    def __init__(self, audio_service, music_name):
        self._music = music_name
        self._audio_service = audio_service
        self._pitch = 0.8

    def execute(self, cast, script):
        self._music_loop()

    def _music_loop(self):
        if self._audio_service.check_sound(self._music) != True:
            self._audio_service.change_pitch(self._music, self._pitch)
            self._audio_service.play_sound(self._music)


    def update_music(self, stage):
        self._pitch = ((stage / 10) % 0.6) + 0.9
        print(self._pitch)
        self._audio_service.change_pitch(self._music, self._pitch)
            

