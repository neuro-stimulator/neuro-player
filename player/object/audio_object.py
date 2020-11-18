from itertools import count

import pygame

from player.object.base_object import BaseObject
from player.object.prefixes import AudioObjectPrefix
from player.state import PlayerState


class AudioObject(BaseObject):
    _ids = count(0)

    def __init__(self, index: int, path: str):
        super().__init__(AudioObjectPrefix + str(next(self._ids)))
        self._index = index
        # self._audio = path
        self._audio = pygame.mixer.Sound(path)
        self._active = False

    def update(self, state: PlayerState):
        if str(self._index) in state.experiment_assets['audio']:
            self._active = state.experiment_assets['audio'][str(self._index)]['active']
        pass

    def draw(self, surface: pygame.Surface, state: PlayerState):
        if self._active:
            self._audio.play()
            # pygame.mixer.music.load(self._audio)
            # pygame.mixer.music.play(0)
            state.experiment_assets['audio'][str(self._index)]['active'] = False
