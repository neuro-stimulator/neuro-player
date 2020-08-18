from cqrs import IEvent

EventName = "StimulatorStateChangeMessageEvent"


class StimulatorStateChangeMessageEvent(IEvent):
    def __init__(self, state: int):
        super().__init__(EventName)
        self._state = state

    @property
    def state(self):
        return self._state
