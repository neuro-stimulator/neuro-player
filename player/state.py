from player.experiment_state import ExperimentState


class PlayerState:
    def __init__(self):
        self._running = True
        self._experiment_state = ExperimentState.EXPERIMENT_READY
        self._public_path = None
        self._experiment_assets = None
        self._objects = []

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running):
        self._running = running

    @property
    def experiment_state(self):
        return self._experiment_state

    @experiment_state.setter
    def experiment_state(self, experiment_state):
        self._experiment_state = experiment_state

    @property
    def public_path(self):
        return self._public_path

    @public_path.setter
    def public_path(self, public_path):
        self._public_path = public_path

    @property
    def experiment_assets(self):
        return self._experiment_assets

    @experiment_assets.setter
    def experiment_assets(self, experiment_assets):
        self._experiment_assets = experiment_assets

    @property
    def objects(self):
        return self._objects
