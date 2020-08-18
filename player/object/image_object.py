from itertools import count

import pygame

from player.object.base_object import BaseObject
from player.state import PlayerState


class ImageObject(BaseObject):
    _ids = count(0)

    def __init__(self, index: int, path: str):
        super().__init__('ImageObject_' + str(next(self._ids)))
        self._index = index
        self._image = pygame.image.load(path)
        self._width = self._image.get_width()
        self._height = self._image.get_height()
        self._active = False

    def update(self, state: PlayerState):
        self._active = state.experiment_assets['image'][str(self._index)]['active']
        pass

    def draw(self, surface: pygame.Surface, state: PlayerState):
        super().update(state)

        if self._active:
            surface.blit(self._image, (50, 50))
            pass
        else:
            pass
