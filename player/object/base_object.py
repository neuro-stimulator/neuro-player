from pygame.surface import Surface

from player.state import PlayerState


class BaseObject:
    def __init__(self, name):
        self._name = name

    def update(self, state: PlayerState):
        pass

    def draw(self, surface: Surface, state: PlayerState):
        pass

    @property
    def name(self):
        return self._name
