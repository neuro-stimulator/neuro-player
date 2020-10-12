class GPIOConfiguration:
    def __init__(self, is_virtual: bool):
        self._is_virtual = is_virtual

    @property
    def is_virtual(self):
        return self._is_virtual
