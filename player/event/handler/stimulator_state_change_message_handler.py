from cqrs import IEventHandler
from player.state import PlayerState

from connection.event.impl.stimulator_state_change_message_event import StimulatorStateChangeMessageEvent


class StimulatorStateChangeMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState):
        self._state = state

    def handle(self, event: StimulatorStateChangeMessageEvent):
        self._state.experiment_state = event.state
