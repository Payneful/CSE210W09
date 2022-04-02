import os
import pathlib
import pyray


class AudioService():
    """A Raylib implementation of AudioService."""

    def __init__(self):
        self._sounds = {}
        
    def initialize(self):
        pyray.init_audio_device()
    
    def load_sounds(self, filepath, name, volume = 1):
        sound = pyray.load_sound(filepath)
        self._sounds[name] = sound
        pyray.set_sound_volume(sound, volume)

    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()

    def play_sound(self, name):
        sound = self._sounds[name]
        pyray.play_sound(sound)
    
    def stop_sound(self, name):
        pyray.stop_sound(name) 

    def check_sound(self, name):
        sound = self._sounds[name]
        return pyray.is_sound_playing(sound)

    def release(self):
        pyray.close_audio_device()

    def change_pitch(self, name, pitch):
        sound = self._sounds[name]
        pyray.set_sound_pitch(sound, pitch)

    def change_volume(self, name, volume):
        sound = self._sounds[name]
        pyray.set_sound_volume(sound, volume)


        
    # def load_sounds(self, directory):
    #     filepaths = self._get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
    #     for filepath in filepaths:
    #         sound = pyray.load_sound(filepath)
    #         self._sounds[filepath] = sound

    # def play_sound(self, sound):
    #     filepath = sound.get_filename()
    #     volume = sound.get_volume()
    #     sound = self._sounds[filepath]
    #     # pyray.set_sound_volume(volume)
    #     pyray.play_sound(sound)
        
    # def unload_sounds(self):
    #     for sound in self._sounds.values():
    #         pyray.unload_sound(sound)
    #     self._sounds.clear()
        
    # def _get_filepaths(self, directory, filter):
    #     filepaths = []
    #     for file in os.listdir(directory):
    #         filename = os.path.join(directory, file)
    #         extension = pathlib.Path(filename).suffix.lower()
    #         if extension in filter:
    #             filepaths.append(filename)
    #     return filepaths


#Sound LoadSound(const char *fileName);        // Load sound from file
#void PlaySound(Sound sound);                  // Play a sound


