class ToServerMessage:
    def __init__(self, topic: str, command_id: int = 0, data=None):
        if data is None:
            data = {}

        self._topic = topic
        self._command_id = command_id
        self._data = data

    def serialize_message(self):
        return {'topic': self._topic, 'commandID': self._command_id, 'data': self._data}
