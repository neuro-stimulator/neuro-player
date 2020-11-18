import logging

from cqrs import ICommandHandler

from player.state import PlayerState
from player.command.impl.clear_objects_command import ClearObjectsCommand


class ClearObjectsHandler(ICommandHandler):
    def __init__(self, state: PlayerState):
        self._state = state

    def execute(self, command: ClearObjectsCommand):
        if command.images and command.sounds and command.texts:
            logging.info("Mažu všechny objekty a resetuji assety.")
            self._state.objects.clear()
            self._state.experiment_assets = None

        if command.texts:
            text_objects = self._state.text_objects
            if len(text_objects) != 0:
                for obj in text_objects:
                    self._state.objects.remove(obj)

        if command.images:
            image_objects = self._state.image_objects
            if len(image_objects) != 0:
                for obj in image_objects:
                    self._state.objects.remove(obj)
                self._state.experiment_assets["images"] = []

        if command.sounds:
            audio_objects = self._state.audio_objects
            if len(audio_objects) != 0:
                for obj in audio_objects:
                    self._state.objects.remove(obj)
                self._state.experiment_assets["audio"] = []
