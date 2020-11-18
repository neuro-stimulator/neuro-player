from itertools import count

import pygame
from pygame.surface import Surface

from player.object.base_object import BaseObject
from player.object.prefixes import TextObjectPrefix
from player.state import PlayerState


class TextObject(BaseObject):
    _ids = count(0)

    def __init__(self, x: int, y: int, text: str, size: int = 36, color=(0, 0, 0)):
        super().__init__(TextObjectPrefix + str(next(self._ids)))
        self._x = x
        self._y = y
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        self._text_surface = font.render(text, antialias=True, color=color)

    def draw(self, surface: Surface, state: PlayerState):
        surface.blit(self._text_surface, dest=(self._x, self._y))

