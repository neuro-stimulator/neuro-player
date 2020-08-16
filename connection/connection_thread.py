import json
import socket
import threading
import time

from cqrs import CQRS


class ConnectionThread(threading.Thread):
    def __init__(self, cqrs: CQRS, port=8080):
        threading.Thread.__init__(self)
        self._running = True
        self._port = port
        self._cqrs = cqrs

    def run(self) -> None:
        print("Starting connection thread...")
        while self._running:
            try:
                print("Zkouším se připojit k serveru...")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    print("Bylo vytvořeno spojení se serverem.")
                    s.connect((socket.gethostname(), self._port))
                    self._handle_connection(s)
                    print("Spojení se serverem bylo ukončeno.")
            except ConnectionRefusedError:
                print("Spojení se nepodařilo vytvořit.")
            except ConnectionResetError:
                print("Spojení bylo přerušeno.")
            finally:
                time.sleep(5)

    def _handle_connection(self, s):
        while 1:
            data = s.recv(1024).decode("utf-8")
            decoded = json.loads(data)
            print(decoded)
            topic = decoded["topic"]
            message_data = decoded["data"]
            self._cqrs.publish_event()
            #
            # if "StimulatorStateChangeMessage" == topic:
            #     self._observer.postEvent(communication_event_state[message_data["state"]])
