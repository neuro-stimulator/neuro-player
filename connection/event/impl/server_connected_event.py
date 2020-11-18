from cqrs import IEvent

EventName = "ServerConnectedEvent"


class ServerConnectedEvent(IEvent):
    def __init__(self, socket):
        super().__init__(EventName)
        self._socket = socket

    @property
    def socket(self):
        return self._socket
