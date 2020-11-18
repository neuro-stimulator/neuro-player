import logging

from cqrs import CQRS, IEventHandler
from connection.event.impl.server_disconnected_event import ServerDisconnectedEvent
from connection.state import ConnectionState


class ServerDisconnectedHandler(IEventHandler):
    def __init__(self, state: ConnectionState, cqrs: CQRS):
        self._cqrs = cqrs
        self._state = state

    def handle(self, event: ServerDisconnectedEvent):
        logging.info("Budu mazat uzavřenou instanci socketu.")
        self._state.server_socket = None
