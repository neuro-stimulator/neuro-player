from cqrs import IEvent

EventName = "ExitMessageEvent"


class ExitMessageEvent(IEvent):
    def __init__(self):
        super().__init__(EventName)
