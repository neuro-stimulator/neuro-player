import socket


class ConnectionState:
    def __init__(self):
        self._server_socket = None
        self._running = False

    @property
    def server_socket(self):
        return self._server_socket

    @server_socket.setter
    def server_socket(self, server_socket: socket):
        self._server_socket = server_socket

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, running: bool):
        self._running = running
