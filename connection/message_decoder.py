from connection.event.impl.experiment_assets_message_event import ExperimentAssetsMessageEvent
from cqrs import IEvent

from connection.event.impl.server_public_path_message_event import ServerPublicPathMessageEvent
from connection.event.impl.stimulator_state_change_message_event import StimulatorStateChangeMessageEvent


def decode_message(message) -> IEvent:
    topic = message["topic"]
    data = message["data"]

    if "ServerPublicPathMessage" == topic:
        return ServerPublicPathMessageEvent(data["publicPath"])
    elif "StimulatorStateChangeMessage" == topic:
        return StimulatorStateChangeMessageEvent(data["state"])
    elif "ExperientAssetsMessage" == topic:
        return ExperimentAssetsMessageEvent(data)

    pass