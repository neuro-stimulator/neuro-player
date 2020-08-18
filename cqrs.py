from rx.subject import Subject


class IBase:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class ICommand(IBase):
    def __init__(self, name):
        super().__init__(name)
        pass


class IQuery(IBase):
    def __init__(self, name):
        super().__init__(name)
        pass


class IEvent(IBase):
    def __init__(self, name):
        super().__init__(name)
        pass


class ICommandHandler:
    def execute(self, command: ICommand):
        pass


class IQueryHandler:
    def execute(self, query: IQuery):
        pass


class IEventHandler:
    def handle(self, event: IEvent):
        pass


class CQRS:
    def __init__(self):
        self._command_bus = Subject()
        self._query_bus = Subject()
        self._event_bus = Subject()

        self._commands = {}
        self._queries = {}
        self._events = {}

        self._subscribe()

    def _subscribe(self):
        def _event_next(event: IEvent):
            handlers = self._events[event.name]
            for handler in handlers:
                handler.handle(event)
        self._event_bus.subscribe(on_next=_event_next)

    def execute_command(self, command: ICommand):
        self._command_bus.on_next(command)

    def execute_query(self, query: IQuery):
        self._query_bus.on_next(query)

    def publish_event(self, event: IEvent):
        self._event_bus.on_next(event)

    def add_command_handler(self, command_name: str, handler: ICommandHandler):
        if command_name not in self._commands:
            self._commands[command_name] = []
        self._commands[command_name].append(handler)

    def add_event_handler(self, event_name: str, handler: IEventHandler):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(handler)
