from gpiozero import Button

from cqrs import CQRS
from gpio.event.impl.asset_change_request_event import AssetChangeRequestEvent


class GPIO:
    def __init__(self, cqrs: CQRS):
        self._cqrs = cqrs
        self._btn_0 = Button(1)
        self._btn_1 = Button(2)
        self._btn_2 = Button(3)
        self._btn_3 = Button(4)
        self._enabled = False
        self._init_handlers()

    def _init_handlers(self):
        self._btn_3.when_activated = lambda: self.pressed()
        pass

    def pressed(self):
        btn_0_active = int(self._btn_0.is_active == True)
        btn_1_active = int(self._btn_1.is_active == True)
        btn_2_active = int(self._btn_2.is_active == True)
        value = btn_0_active | btn_1_active << 1 | btn_2_active << 2
        self._enabled = not self._enabled
        self._cqrs.publish_event(AssetChangeRequestEvent(value, self._enabled))
