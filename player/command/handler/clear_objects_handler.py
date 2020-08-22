import logging

from cqrs import ICommandHandler, ICommand

from player.state import PlayerState


class ClearObjectsHandler(ICommandHandler):
    def __init__(self, state: PlayerState):
        self._state = state

    def execute(self, command: ICommand):
        logging.info("Mažu všechny objekty a resetuji assety.")
        self._state.objects.clear()
        self._state.experiment_assets = None
