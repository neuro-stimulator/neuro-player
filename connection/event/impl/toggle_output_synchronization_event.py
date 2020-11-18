from cqrs import IEvent

EventName = "ToggleOutputSynchronizationEvent"


class ToggleOutputSynchronizationEvent(IEvent):
    def __init__(self, command_id: int, synchronize: bool):
        super().__init__(EventName)
        self._command_id = command_id
        self._synchronize = synchronize

    @property
    def command_id(self):
        return self._command_id

    @property
    def synchronize(self):
        return self._synchronize
