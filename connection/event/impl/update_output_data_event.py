from cqrs import IEvent

EventName = "UpdateOutputDataEvent"


class UpdateOutputDataEvent(IEvent):
    def __init__(self, x: int, y: int, type: str, id: int):
        super().__init__(EventName)
        self._x = x
        self._y = y
        self._type = type
        self._id = id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id
