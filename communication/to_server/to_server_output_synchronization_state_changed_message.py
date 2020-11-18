from communication.to_server.to_server_message import ToServerMessage

Topic = "OutputSynchronizationStateChangedMessage"


class ToServerOutputSynchronizationStateChangedMessage(ToServerMessage):
    def __init__(self, command_id: int, success: bool, synchronize: bool):
        super().__init__(Topic, command_id, data={'success': success, 'synchronize': synchronize})
