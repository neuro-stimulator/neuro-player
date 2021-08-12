import logging
import json

from cqrs import CQRS, ICommandHandler
from connection.command.impl.stop_connection_thread_command import StopConnectionThreadCommand

from connection.state import ConnectionState


class StopConnectionThreadHandler(ICommandHandler):
    def __init__(self, state: ConnectionState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def execute(self, command: StopConnectionThreadCommand):
        self._state.running = False
