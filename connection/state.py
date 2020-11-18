import socket


class ConnectionState:
    def __init__(self):
        self._server_socket = None

    @property
    def server_socket(self):
        return self._server_socket

    @server_socket.setter
    def server_socket(self, server_socket: socket):
        self._server_socket = server_socket
