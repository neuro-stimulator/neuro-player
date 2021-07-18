import logging
import sys

from gpio.gpio import GPIO
from gpio.gpio_configuration import GPIOConfiguration
from player.asset_player import AssetPlayer
from connection.connection_thread import ConnectionThread
from cqrs import CQRS


def main(argv):
    if len(argv) != 7:
        print("main.py <server_url> <server_port> <width> <height> <frame_rate> <fullscreen> <log_file_path>")
        print("length = " + str(len(argv)))
        print(argv)
        sys.exit(2)

    server_address = argv[0]
    server_port = int(argv[1])
    width = int(argv[2])
    height = int(argv[3])
    frame_rate = int(argv[4])
    fullscreen = bool(int(argv[5]))
    log_file_path = argv[6]

    logging.basicConfig(
        handlers=[logging.FileHandler(filename=log_file_path, encoding='utf-8', mode='w')],
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info("Vytvářím CQRS instanci.")
    cqrs = CQRS()

    logging.info("Inicializuji přehrávač.")
    player = AssetPlayer("Asset player", width, height, frame_rate, fullscreen, cqrs)

    logging.info("Inicializuji GPIO.")
    gpio_configuration = GPIOConfiguration(True)
    gpio = GPIO(gpio_configuration, cqrs)

    logging.info("Inicializuji komunikační vlákno")
    conn_thread = ConnectionThread(cqrs, server_address, server_port)
    conn_thread.setDaemon(True)
    conn_thread.start()

    logging.info("Spouštím přehrávač.")
    player.run()


if __name__ == "__main__":
    main(sys.argv[1:])
