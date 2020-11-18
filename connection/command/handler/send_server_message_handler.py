import logging
import json

from cqrs import CQRS, ICommandHandler

from connection.state import ConnectionState
from connection.command.impl.send_server_message_command import SendServerMessageCommand


class SendServerMessageHandler(ICommandHandler):
    def __init__(self, state: ConnectionState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def execute(self, command: SendServerMessageCommand):
        js = json.dumps(command.message)
        logging.debug("to server <<< " + js)
        self._state.server_socket.sendall(bytes(js, encoding="utf-8"))
