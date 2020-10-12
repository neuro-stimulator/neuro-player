from cqrs import IEvent

EventName = "ToggleOutputMessageEvent"


class ToggleOutputMessageEvent(IEvent):
    def __init__(self, index):
        super().__init__(EventName)
        self._index = str(index)

    @property
    def index(self):
        return self._index
