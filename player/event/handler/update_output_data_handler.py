import logging

from cqrs import CQRS, IEventHandler

from player.state import PlayerState

from connection.event.impl.update_output_data_event import UpdateOutputDataEvent


class UpdateOutputDataHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state
        self._cqrs = cqrs

    def handle(self, event: UpdateOutputDataEvent):
        logging.debug("Aktualizuji data jednoho výstupu.")
        output = self._state.experiment_assets[event.type][event.id]
        output["x"] = event.x
        output["y"] = event.y
