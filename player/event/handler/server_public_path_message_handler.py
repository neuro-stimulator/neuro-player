from cqrs import IEventHandler
from player.state import PlayerState

from connection.event.impl.server_public_path_message_event import ServerPublicPathMessageEvent


class ServerPublicPathMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState):
        self._state = state

    def handle(self, event: ServerPublicPathMessageEvent):
        self._state.public_path = event.path
        pass
