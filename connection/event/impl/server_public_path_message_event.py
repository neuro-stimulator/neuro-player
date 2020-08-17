from cqrs import IEvent

EventName = "ServerPublicPathMessageEvent"


class ServerPublicPathMessageEvent(IEvent):
    def __init__(self, path):
        super().__init__(EventName)
        self._path = path

    @property
    def path(self):
        return self._path
