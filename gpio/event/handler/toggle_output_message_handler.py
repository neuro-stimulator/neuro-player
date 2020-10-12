import logging

from cqrs import CQRS, IEventHandler

from connection.event.impl.toggle_output_message_event import ToggleOutputMessageEvent
from gpio.event.impl.asset_change_request_event import AssetChangeRequestEvent


class ToggleOutputMessageHandler(IEventHandler):
    def __init__(self, cqrs: CQRS):
        self._cqrs = cqrs
        self._enabled = False

    def handle(self, command: ToggleOutputMessageEvent):
        logging.info("Budu přepínat výstup na základě podnětu z virtuálního stimulátoru.")
        self._enabled = not self._enabled
        self._cqrs.publish_event(AssetChangeRequestEvent(command.index, self._enabled))
