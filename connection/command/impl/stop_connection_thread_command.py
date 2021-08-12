from cqrs import ICommand

CommandName = "StopConnectionThreadCommand"


class StopConnectionThreadCommand(ICommand):
    def __init__(self):
        super().__init__(CommandName)
