import logging

from cqrs import CQRS, IEventHandler

from player.state import PlayerState
from player.command.impl.clear_objects_command import ClearObjectsCommand

from connection.event.impl.toggle_output_synchronization_event import ToggleOutputSynchronizationEvent
from connection.command.impl.send_server_message_command import SendServerMessageCommand

from communication.to_server.to_server_output_synchronization_state_changed_message import \
    ToServerOutputSynchronizationStateChangedMessage


class ToggleOutputSynchronizationHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def handle(self, event: ToggleOutputSynchronizationEvent):
        logging.debug("Přepínám synchronizaci výstupů.")
        self._state.synchronizeOutputs = event.synchronize
        if not event.synchronize:
            self._cqrs.execute_command(ClearObjectsCommand(texts=False))
        self._cqrs.execute_command(SendServerMessageCommand(
            ToServerOutputSynchronizationStateChangedMessage(event.command_id, True, event.synchronize)))
