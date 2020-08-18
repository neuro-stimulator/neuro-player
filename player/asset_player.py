import json
import sys
import pprint

import pygame
from collections import defaultdict

from cqrs import CQRS
from player.object.image_object import ImageObject
from player.state import PlayerState

from connection.event.impl.server_public_path_message_event import EventName as ServerPublicPathMessageEventName
from connection.event.impl.stimulator_state_change_message_event import EventName as StimulatorStateChangeMessageEventName
from connection.event.impl.experiment_assets_message_event import EventName as ExperimentAssetsMessageEventName

from player.event.handler.server_public_path_message_handler import ServerPublicPathMessageHandler
from player.event.handler.stimulator_state_change_message_handler import StimulatorStateChangeMessageHandler
from player.event.handler.experiment_assets_message_handler import ExperimentAssetsMessageHandler

EVENTS = {
    ServerPublicPathMessageEventName: ServerPublicPathMessageHandler,
    StimulatorStateChangeMessageEventName: StimulatorStateChangeMessageHandler,
    ExperimentAssetsMessageEventName: ExperimentAssetsMessageHandler
}


class AssetPlayer:
    def __init__(self, caption: str, width: int, height: int, frame_rate: int, cqrs: CQRS):
        self.frame_rate = frame_rate
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
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
            pass

        def _init_event_handlers():
            for event in EVENTS:
                self._cqrs.add_event_handler(event, EVENTS[event](self._state))
            pass

        def _init_query_handlers():
            pass

        def _init_key_handlers():
            def func(key):
                # self._state.objects[0].active = not self._state.objects[0].active
                self._state.experiment_assets['image']['0']['active'] = not self._state.experiment_assets['image']['0']['active']
            pass

            self.keyup_handlers[pygame.HWACCEL].append(func)

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
                self._pp.pprint(self._state.__dict__)
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
