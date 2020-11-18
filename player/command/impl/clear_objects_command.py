from cqrs import ICommand

CommandName = "ClearObjectsCommand"


class ClearObjectsCommand(ICommand):
    def __init__(self, images: bool = True, sounds: bool = True, texts: bool = True):
        super().__init__(CommandName)
        self._images = images
        self._sounds = sounds
        self._texts = texts

    @property
    def images(self):
        return self._images

    @property
    def sounds(self):
        return self._sounds

    @property
    def texts(self):
        return self._texts
