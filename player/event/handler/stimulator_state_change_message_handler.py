from cqrs import CQRS, IEventHandler
from player.experiment_state import ExperimentState
from player.state import PlayerState

from connection.event.impl.stimulator_state_change_message_event import StimulatorStateChangeMessageEvent
from player.command.impl.clear_objects_command import ClearObjectsCommand


class StimulatorStateChangeMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def handle(self, event: StimulatorStateChangeMessageEvent):
        self._state.experiment_state = event.state
        if event.state == ExperimentState.EXPERIMENT_CLEAR:
            self._cqrs.execute_command(ClearObjectsCommand())
