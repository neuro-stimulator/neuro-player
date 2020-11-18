from cqrs import ICommand
from communication.to_server.to_server_message import ToServerMessage

CommandName = "SendServerMessageCommand"


class SendServerMessageCommand(ICommand):
    def __init__(self, message: ToServerMessage):
        super().__init__(CommandName)
        self._message = message

    @property
    def message(self):
        return self._message.serialize_message()
