import logging

from cqrs import IEventHandler, CQRS
from gpio.event.impl.asset_change_request_event import AssetChangeRequestEvent

from player.state import PlayerState


class AssetChangeRequestHandler(IEventHandler):
    def __init__(self, state: PlayerState, cqrs: CQRS):
        self._state = state  # type: { 'audio': {}, 'image': {} }
        self._cqrs = cqrs

    def handle(self, event: AssetChangeRequestEvent):
        if 'image' in self._state.experiment_assets:
            if event.index in self._state.experiment_assets['image']:
                self._state.experiment_assets['image'][event.index]['active'] = event.enabled
                logging.debug('image[' + event.index + '].active = ' + str(event.enabled))
        if 'audio' in self._state.experiment_assets:
            if event.index in self._state.experiment_assets['audio']:
                self._state.experiment_assets['audio'][event.index]['active'] = event.enabled
                logging.debug('audio[' + event.index + '].active = ' + str(event.enabled))
