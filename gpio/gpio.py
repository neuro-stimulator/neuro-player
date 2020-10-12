import logging
from gpiozero import Button

from cqrs import CQRS

from connection.event.impl.toggle_output_message_event import EventName as ToggleOutputMessageEventName

from gpio.event.impl.asset_change_request_event import AssetChangeRequestEvent
from gpio.event.handler.toggle_output_message_handler import ToggleOutputMessageHandler
from gpio.gpio_configuration import GPIOConfiguration

COMMANDS = {

}

EVENTS = {
    ToggleOutputMessageEventName: ToggleOutputMessageHandler
}


class GPIO:
    def __init__(self, gpio_configuration: GPIOConfiguration, cqrs: CQRS):
        self._gpio_configuration = gpio_configuration
        self._cqrs = cqrs
        if not self._gpio_configuration.is_virtual:
            self._btn_0 = Button(1)
            self._btn_1 = Button(2)
            self._btn_2 = Button(3)
            self._btn_3 = Button(4)
        self._enabled = False
        self._init_handlers()

    def _init_handlers(self):

        def _init_command_handlers():
            for command in COMMANDS:
                logging.debug("Inicializuji command handler: " + command)
            pass

        def _init_event_handlers():
            for event in EVENTS:
                logging.debug("Inicializuji event handler: " + event)
                self._cqrs.add_event_handler(event, EVENTS[event](self._cqrs))
            pass

        def _init_query_handlers():
            pass

        def _init_button_handlers():
            logging.debug("Inicializuji handlery na GPIO vstupy")
            self._btn_3.when_activated = lambda: self.pressed()

        _init_command_handlers()
        _init_event_handlers()
        _init_query_handlers()
        if not self._gpio_configuration.is_virtual:
            _init_button_handlers()

    def pressed(self):
        btn_0_active = int(self._btn_0.is_active == True)
        btn_1_active = int(self._btn_1.is_active == True)
        btn_2_active = int(self._btn_2.is_active == True)
        value = btn_0_active | btn_1_active << 1 | btn_2_active << 2
        self._enabled = not self._enabled
        self._cqrs.publish_event(AssetChangeRequestEvent(value, self._enabled))
