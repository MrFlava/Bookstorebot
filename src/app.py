import os
import logging
from src.settings import MEDIA_FOLDER, RESOURCES_FOLDER
from botmanlib.bot import BotmanBot
from src.dbscripts.send_to_users import sends_handler
from src.dbscripts.add_book import record_handler
from src.dbscripts.orders import exist_handler, notexist_handler
from src.dbscripts.change_desc import desc_handler
from src.dbscripts.delete_book import delete_handler
from src.menus.startmenu import Menus
from src.menus.admmenu import Admmenu
from telegram.ext import Updater
logger = logging.getLogger(__name__)
def main():
    bot_token = os.environ['bot.token']
    bot = BotmanBot(token=bot_token)
    updater = Updater(bot=bot)
    dp = updater.dispatcher
    start_menu = Menus(bot=bot, dispatcher=dp)
    adm_menu = Admmenu(bot=bot, dispatcher=dp)
    dp.add_handler(sends_handler)
    dp.add_handler(start_menu.handler)
    dp.add_handler(adm_menu.handler)
    dp.add_handler(delete_handler)
    dp.add_handler(exist_handler)
    dp.add_handler(notexist_handler)
    dp.add_handler(record_handler)
    dp.add_handler(desc_handler)

    if not os.path.exists(MEDIA_FOLDER):
        os.mkdir(MEDIA_FOLDER)
        logger.info("Media folder created")
    if not os.path.exists(RESOURCES_FOLDER):
        os.mkdir(RESOURCES_FOLDER)
        logger.info("Resources folder created")

    logger.info("Bot started")

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
