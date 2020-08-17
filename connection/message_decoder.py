from connection.event.impl.server_public_path_message_event import ServerPublicPathMessageEvent
from cqrs import IEvent


def decode_message(message) -> IEvent:
    topic = message["topic"]
    data = message["data"]

    if "ServerPublicPathMessage" == topic:
        return ServerPublicPathMessageEvent(data["publicPath"])

    pass