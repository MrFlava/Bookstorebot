import os
from botmanlib.bot import BotmanBot
from src.send_to_users import sends_handler
from src.dbscripts.add_book import record_handler
from src.dbscripts.orders import exist_handler, notexist_handler
from src.dbscripts.change_desc import  desc_handler
from src.dbscripts.delete_book import delete_handler
from src.menus.menus import menu_handler, admkeyboard_handler
from telegram.ext import Updater
def main():
    bot_token = os.environ['bot.token']
    bot = BotmanBot(token=bot_token)
    updater = Updater(bot=bot)
    dp = updater.dispatcher
    dp.add_handler(sends_handler)
    dp.add_handler(menu_handler)
    dp.add_handler(admkeyboard_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(exist_handler)
    dp.add_handler(notexist_handler)
    dp.add_handler(record_handler)
    dp.add_handler(desc_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
