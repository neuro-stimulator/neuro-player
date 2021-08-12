from cqrs import IEvent

from connection.event.impl.experiment_assets_message_event import ExperimentAssetsMessageEvent
from connection.event.impl.server_public_path_message_event import ServerPublicPathMessageEvent
from connection.event.impl.stimulator_state_change_message_event import StimulatorStateChangeMessageEvent
from connection.event.impl.toggle_output_message_event import ToggleOutputMessageEvent
from connection.event.impl.toggle_output_synchronization_event import ToggleOutputSynchronizationEvent
from connection.event.impl.unknown_message_event import UnknownMessageEvent
from connection.event.impl.update_output_data_event import UpdateOutputDataEvent
from connection.event.impl.exit_message_event import ExitMessageEvent


def decode_message(message) -> IEvent:
    topic = message["topic"]
    command_id = message["commandID"]
    data = message["data"]

    if "ServerPublicPathMessage" == topic:
        return ServerPublicPathMessageEvent(data["publicPath"])
    elif "StimulatorStateChangeMessage" == topic:
        return StimulatorStateChangeMessageEvent(data["state"])
    elif "ExperientAssetsMessage" == topic:
        return ExperimentAssetsMessageEvent(data)
    elif "ToggleOutputMessage" == topic:
        return ToggleOutputMessageEvent(data["index"])
    elif "ToggleOutputSynchronizationMessage" == topic:
        return ToggleOutputSynchronizationEvent(command_id, data["synchronize"])
    elif "UpdateOutputDataMessage" == topic:
        return UpdateOutputDataEvent(data["x"], data["y"], data["type"], data["id"])
    elif "ExitMessage" == topic:
        return ExitMessageEvent()
    else:
        return UnknownMessageEvent()

    pass
