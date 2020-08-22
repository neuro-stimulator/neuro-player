from itertools import count

import pygame

from player.object.base_object import BaseObject
from player.state import PlayerState


class AudioObject(BaseObject):
    _ids = count(0)

    def __init__(self, index: int, path: str):
        super().__init__('AudioObject' + str(next(self._ids)))
        self._index = index
        self._audio = path
        self._active = False

    def update(self, state: PlayerState):
        self._active = state.experiment_assets['audio'][str(self._index)]['active']
        pass

    def draw(self, surface: pygame.Surface, state: PlayerState):
        if self._active:
            pygame.mixer.music.load(self._audio)
            pygame.mixer.music.play()
