import logging
import json
import socket
import threading
import time

from cqrs import CQRS
from connection.state import ConnectionState
from connection.message_decoder import decode_message

from connection.command.impl.send_server_message_command import CommandName as SendServerMessageCommandName
from connection.event.impl.server_connected_event import EventName as ServerConnectedEventName
from connection.event.impl.server_disconnected_event import EventName as ServerDisonnectedEventName
from connection.event.impl.unknown_message_event import EventName as UnknownMessageEventName

from connection.event.impl.server_connected_event import ServerConnectedEvent
from connection.event.impl.server_disconnected_event import ServerDisconnectedEvent

from connection.event.handler.server_connected_handler import ServerConnectedHandler
from connection.event.handler.server_disconnected_handler import ServerDisconnectedHandler
from connection.event.handler.unknown_message_handler import UnknownMessageHandler
from connection.command.handler.send_server_message_handler import SendServerMessageHandler

COMMANDS = {
    SendServerMessageCommandName: SendServerMessageHandler
}

EVENTS = {
    ServerConnectedEventName: ServerConnectedHandler,
    ServerDisonnectedEventName: ServerDisconnectedHandler,
    UnknownMessageEventName: UnknownMessageHandler
}


class ConnectionThread(threading.Thread):
    def __init__(self, cqrs: CQRS, address: str = "localhost", port: int = 8080):
        threading.Thread.__init__(self)
        self._running = True
        self._address = address
        self._port = port
        self._cqrs = cqrs
        self._state = ConnectionState()
        self._init_handlers()

    def _init_handlers(self):
        def _init_command_handlers():
            for command in COMMANDS:
                logging.debug("Inicializuji command handler: " + command)
                self._cqrs.add_command_handler(command, COMMANDS[command](self._state, self._cqrs))
            pass

        def _init_event_handlers():
            for event in EVENTS:
                logging.debug("Inicializuji event handler: " + event)
                self._cqrs.add_event_handler(event, EVENTS[event](self._state, self._cqrs))
            pass

        def _init_query_handlers():
            pass

        _init_command_handlers()
        _init_event_handlers()
        _init_query_handlers()

    def run(self) -> None:
        logging.info("Starting connection thread...")
        while self._running:
            try:
                logging.info("Zkouším se připojit k serveru: " + self._address + ":" + str(self._port))
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self._address, self._port))
                    logging.info("Bylo vytvořeno spojení se serverem.")
                    self._cqrs.publish_event(ServerConnectedEvent(s))
                    self._handle_connection(s)
                    logging.info("Spojení se serverem bylo ukončeno.")
                    self._cqrs.publish_event(ServerDisconnectedEvent())
            except ConnectionRefusedError:
                logging.warning("Spojení se nepodařilo vytvořit.")
            except ConnectionResetError:
                logging.error("Spojení bylo přerušeno.")
                self._cqrs.publish_event(ServerDisconnectedEvent())
            finally:
                time.sleep(5)

    def _handle_connection(self, s: socket):
        while 1:
            data = s.recv(1024).decode("utf-8")
            parsed = json.loads(data)
            logging.debug("from server >>> " + data)
            event = decode_message(parsed)
            self._cqrs.publish_event(event)
