import logging
from asset_player import AssetPlayer

logging.info("Inicializuji přehrávač")

player = AssetPlayer("Asset player", 800, 600, 30)
player.run()
logging.info("Čekám na další zprávy")