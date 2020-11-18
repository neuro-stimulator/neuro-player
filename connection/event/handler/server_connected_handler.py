import logging

from cqrs import CQRS, IEventHandler
from connection.event.impl.server_connected_event import ServerConnectedEvent
from connection.state import ConnectionState


class ServerConnectedHandler(IEventHandler):
    def __init__(self, state: ConnectionState, cqrs: CQRS):
        self._cqrs = cqrs
        self._state = state

    def handle(self, event: ServerConnectedEvent):
        logging.info("Budu ukládat instanci socketu pro budoucí použití.")
        self._state.server_socket = event.socket
