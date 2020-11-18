import logging

from gpio.gpio import GPIO
from gpio.gpio_configuration import GPIOConfiguration
from player.asset_player import AssetPlayer
from connection.connection_thread import ConnectionThread
from cqrs import CQRS

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

logging.info("Vytvářím CQRS instanci.")
cqrs = CQRS()

logging.info("Inicializuji přehrávač.")
player = AssetPlayer("Asset player", 800, 600, 60, cqrs)

logging.info("Inicializuji GPIO.")
gpio_configuration = GPIOConfiguration(True)
gpio = GPIO(gpio_configuration, cqrs)

logging.info("Inicializuji komunikační vlákno")
connThread = ConnectionThread(cqrs, 8080)
connThread.setDaemon(True)
connThread.start()

logging.info("Spouštím přehrávač.")
player.run()
