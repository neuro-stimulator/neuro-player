from cqrs import IEvent

EventName = "ExperimentAssetsMessageEvent"


class ExperimentAssetsMessageEvent(IEvent):
    def __init__(self, data):
        super().__init__(EventName)
        self._data = data

    @property
    def data(self):
        return self._data