from local_settings import Token
from menus.menus import menus_handler
from telegram.ext import Updater
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(menus_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
