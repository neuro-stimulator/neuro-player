from cqrs import IEvent

from connection.event.impl.experiment_assets_message_event import ExperimentAssetsMessageEvent
from connection.event.impl.server_public_path_message_event import ServerPublicPathMessageEvent
from connection.event.impl.stimulator_state_change_message_event import StimulatorStateChangeMessageEvent
from connection.event.impl.toggle_output_message_event import ToggleOutputMessageEvent


def decode_message(message) -> IEvent:
    topic = message["topic"]
    data = message["data"]

    if "ServerPublicPathMessage" == topic:
        return ServerPublicPathMessageEvent(data["publicPath"])
    elif "StimulatorStateChangeMessage" == topic:
        return StimulatorStateChangeMessageEvent(data["state"])
    elif "ExperientAssetsMessage" == topic:
        return ExperimentAssetsMessageEvent(data)
    elif "ToggleOutputMessage" == topic:
        return ToggleOutputMessageEvent(data["index"])

    pass