import logging

from os import path
from cqrs import IEventHandler, CQRS

from player.object.audio_object import AudioObject
from player.object.image_object import ImageObject
from player.state import PlayerState

from connection.event.impl.experiment_assets_message_event import ExperimentAssetsMessageEvent


class ExperimentAssetsMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state  # type: { 'audio': {}, 'image': {} }

    def handle(self, event: ExperimentAssetsMessageEvent):
        logging.debug("Přepisuji seznam všech mediálních souborů.")
        self._state.experiment_assets = {}
        for assetType in event.data:
            assets = event.data[assetType]
            self._state.experiment_assets[assetType] = {}
            for assetIndex in assets:
                entry = assets[assetIndex]
                self._state.experiment_assets[assetType][assetIndex] = {
                    'entry': entry['name'],
                    'active': True,
                    'x': entry['x'],
                    'y': entry['y']
                }
                if 'audio' == assetType:
                    self._state.objects.append(
                        AudioObject(assetIndex, path.join(self._state.public_path, entry['name']))
                    )
                    pass
                elif 'image' == assetType:
                    self._state.objects.append(
                        ImageObject(assetIndex, path.join(self._state.public_path, entry['name']))
                    )
