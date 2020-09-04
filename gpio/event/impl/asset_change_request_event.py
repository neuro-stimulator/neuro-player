from cqrs import IEvent


EventName = "AssetChangeRequestEvent"


class AssetChangeRequestEvent(IEvent):
    def __init__(self, index, enabled):
        self._index = index
        self._enabled = enabled
        super().__init__(EventName)

    @property
    def index(self):
        return self._index

    @property
    def enabled(self):
        return self._enabled
