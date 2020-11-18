from cqrs import IEvent

EventName = "ServerDisconnectedEvent"


class ServerDisconnectedEvent(IEvent):
    def __init__(self):
        super().__init__(EventName)
