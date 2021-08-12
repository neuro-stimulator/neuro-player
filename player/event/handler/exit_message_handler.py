import logging

from cqrs import IEventHandler, CQRS
from connection.event.impl.exit_message_event import ExitMessageEvent

from player.state import PlayerState


class ExitMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def handle(self, event: ExitMessageEvent):
        self._state.running = False
