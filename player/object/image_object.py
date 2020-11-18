from itertools import count

import pygame

from player.object.base_object import BaseObject
from player.object.prefixes import ImageObjectPrefix
from player.state import PlayerState


class ImageObject(BaseObject):
    _ids = count(0)

    def __init__(self, index: int, path: str):
        super().__init__(ImageObjectPrefix + str(next(self._ids)))
        self._index = index
        self._image = pygame.image.load(path)
        self._width = self._image.get_width()
        self._height = self._image.get_height()
        self._active = False
        self._x = 50
        self._y = 50

    def update(self, state: PlayerState):
        if str(self._index) in state.experiment_assets['image']:
            self._active = state.experiment_assets['image'][str(self._index)]['active']
            self._x = state.experiment_assets['image'][str(self._index)]["x"]
            self._y = state.experiment_assets['image'][str(self._index)]["y"]
        pass

    def draw(self, surface: pygame.Surface, state: PlayerState):
        super().update(state)

        if self._active:
            surface.blit(self._image, (self._x, self._y))
            pass
        else:
            pass
