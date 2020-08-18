from cqrs import IEventHandler
from player.object.image_object import ImageObject
from player.state import PlayerState

from connection.event.impl.experiment_assets_message_event import ExperimentAssetsMessageEvent


class ExperimentAssetsMessageHandler(IEventHandler):
    def __init__(self, state: PlayerState):
        self._state = state  # type: { 'audio': {}, 'image': {} }

    def handle(self, event: ExperimentAssetsMessageEvent):
        # for audioIndex in event.data['audio']:
        #     audio = event.data['audio'][audioIndex]  # type: str

        # for image_index in event.data['image']:
        #     image = event.data['image'][image_index]
        #     obj = ImageObject(image_index, self._state.public_path + '/' + image)
        #     self._state.objects.append(obj)
        #     self._state.experiment_assets['audio'][audioIndex] = {'entry': audio, 'active': False}

        self._state.experiment_assets = {}
        for assetType in event.data:
            assets = event.data[assetType]
            self._state.experiment_assets[assetType] = {}
            for assetIndex in assets:
                entry = assets[assetIndex]
                self._state.experiment_assets[assetType][assetIndex] = {'entry': entry, 'active': False}
                self._state.objects.append(ImageObject(assetIndex, self._state.public_path + '/' + entry))
        # self._state.experiment_assets = event.data
