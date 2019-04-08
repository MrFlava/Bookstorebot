from local_settings import Token
from send_to_users import sends_handler
from dbscripts.add_book import record_handler
from dbscripts.orders import exist_handler, notexist_handler
from dbscripts.delete_book import delete_handler
from menus.menus import menu_handler, admkeyboard_handler
from telegram.ext import Updater
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(sends_handler)
    dp.add_handler(menu_handler)
    dp.add_handler(admkeyboard_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(exist_handler)
    dp.add_handler(notexist_handler)
    dp.add_handler(record_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
