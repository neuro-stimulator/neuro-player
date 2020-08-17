import logging
from player.asset_player import AssetPlayer
from connection.connection_thread import ConnectionThread
from cqrs import CQRS

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

# pipe = sys.argv[1]
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((socket.gethostname(), 8080))
#     while 1:
#         data = s.recv(1024).decode("utf-8")
#         decoded = json.loads(data)
#         print(decoded)


# server = open(pipe, 'r')
#
# while server.readable():
#     command = server.read()
#     print(command)
#
# print("Konec")

logging.basicConfig(level=logging.DEBUG)

logging.info("Inicializuji komunikační vlákno")

logging.info("Inicializuji přehrávač")

cqrs = CQRS()

player = AssetPlayer("Asset player", 800, 600, 30, cqrs)

connThread = ConnectionThread(cqrs, 8080)
connThread.setDaemon(True)
connThread.start()

player.run()
