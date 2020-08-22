from cqrs import ICommand

CommandName = "ClearObjectsCommand"


class ClearObjectsCommand(ICommand):
    def __init__(self):
        super().__init__(CommandName)