import logging

from cqrs import CQRS, IEventHandler
from connection.event.impl.unknown_message_event import UnknownMessageEvent


class UnknownMessageHandler(IEventHandler):
    def __init__(self, state, cqrs: CQRS):
        pass

    def handle(self, event: UnknownMessageEvent):
        logging.warning("Přišla nerozpoznaná zpráva ze serveru!")
