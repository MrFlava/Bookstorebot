from local_settings import Token
from dbscripts.delete_book import delete_handler
from menus.menus import menus_handler, admkeyboard_handler
from telegram.ext import Updater
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(menus_handler)
     dp.add_handler(admkeyboard_handler)
    dp.add_handler(delete_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
