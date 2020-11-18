from cqrs import IEvent

EventName = "UnknownMessageEvent"


class UnknownMessageEvent(IEvent):
    def __init__(self):
        super().__init__(EventName)
