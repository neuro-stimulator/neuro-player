import logging
import sys
import pprint

import pygame
from collections import defaultdict

from cqrs import CQRS
from player.state import PlayerState

from player.command.impl.clear_objects_command import CommandName as ClearObjectsCommandName
from connection.event.impl.server_public_path_message_event import EventName as ServerPublicPathMessageEventName
from connection.event.impl.stimulator_state_change_message_event import EventName as StimulatorStateChangeMessageEventName
from connection.event.impl.experiment_assets_message_event import EventName as ExperimentAssetsMessageEventName
from connection.event.impl.toggle_output_synchronization_event import EventName as ToggleOutputSynchronizationEventName
from connection.event.impl.update_output_data_event import EventName as UpdateOutputDataEventName
from connection.event.impl.exit_message_event import EventName as ExitMessageEventName
from gpio.event.impl.asset_change_request_event import EventName as AssetChangeRequestEventName

from player.command.handler.clear_objects_handler import ClearObjectsHandler
from player.event.handler.server_public_path_message_handler import ServerPublicPathMessageHandler
from player.event.handler.stimulator_state_change_message_handler import StimulatorStateChangeMessageHandler
from player.event.handler.experiment_assets_message_handler import ExperimentAssetsMessageHandler
from player.event.handler.asset_change_request_handler import AssetChangeRequestHandler
from player.event.handler.toggle_output_synchronization_handler import ToggleOutputSynchronizationHandler
from player.event.handler.update_output_data_handler import UpdateOutputDataHandler
from player.event.handler.exit_message_handler import ExitMessageHandler

from connection.command.impl.stop_connection_thread_command import StopConnectionThreadCommand

COMMANDS = {
    ClearObjectsCommandName: ClearObjectsHandler
}

EVENTS = {
    ServerPublicPathMessageEventName: ServerPublicPathMessageHandler,
    StimulatorStateChangeMessageEventName: StimulatorStateChangeMessageHandler,
    ExperimentAssetsMessageEventName: ExperimentAssetsMessageHandler,
    AssetChangeRequestEventName: AssetChangeRequestHandler,
    ToggleOutputSynchronizationEventName: ToggleOutputSynchronizationHandler,
    UpdateOutputDataEventName: UpdateOutputDataHandler,
    ExitMessageEventName: ExitMessageHandler
}


class AssetPlayer:
    def __init__(self, caption: str, width: int, height: int, frame_rate: int, fullscreen: bool, cqrs: CQRS):
        self.frame_rate = frame_rate
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        flags = 0
        if fullscreen:
            flags = pygame.FULLSCREEN
        self.surface = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self._cqrs = cqrs
        self._state = PlayerState()
        self._init_handlers()
        self._pp = pprint.PrettyPrinter(depth=4)

    def _init_handlers(self):
        def _init_command_handlers():
            for command in COMMANDS:
                logging.debug("Inicializuji command handler: " + command)
                self._cqrs.add_command_handler(command, COMMANDS[command](self._state))
            pass

        def _init_event_handlers():
            for event in EVENTS:
                logging.debug("Inicializuji event handler: " + event)
                self._cqrs.add_event_handler(event, EVENTS[event](self._state, self._cqrs))
            pass

        def _init_query_handlers():
            pass

        def _init_key_handlers():
            def sys_exit(key):
                pygame.quit()
                sys.exit(0)

            self.keyup_handlers[pygame.K_q].append(sys_exit)

        _init_command_handlers()
        _init_event_handlers()
        _init_query_handlers()
        _init_key_handlers()

    def update(self):
        for o in self._state.objects:
            o.update(self._state)

    def draw(self):
        for o in self._state.objects:
            o.draw(self.surface, self._state)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while self._state.running:
            self.surface.fill((255, 255, 255))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
        logging.info("Byla ukončena hlavní programová smyčka. Zahajuji ukončovací fázi.")
        self._cqrs.execute_command(StopConnectionThreadCommand())
        pygame.quit()
        exit()
