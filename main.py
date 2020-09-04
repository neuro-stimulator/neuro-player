import logging

from gpio.gpio import GPIO
from player.asset_player import AssetPlayer
from connection.connection_thread import ConnectionThread
from cqrs import CQRS

logging.basicConfig(level=logging.DEBUG)

logging.info("Vytvářím CQRS instanci.")
cqrs = CQRS()

logging.info("Inicializuji přehrávač.")
player = AssetPlayer("Asset player", 800, 600, 60, cqrs)

logging.info("Inicializuji GPIO.")
gpio = GPIO(cqrs)

logging.info("Inicializuji komunikační vlákno")
connThread = ConnectionThread(cqrs, 8080)
connThread.setDaemon(True)
connThread.start()

logging.info("Spouštím přehrávač.")
player.run()
