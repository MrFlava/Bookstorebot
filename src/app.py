from local_settings import Token
"""
from dbscripts.orders import  get_order
from send_to_users import send_messages
from dbscripts.add_book import  get_new_books
from dbscripts.change_desc import  new_description
"""
# это не имеет смысла, если я подключу conv-handler-ы

from dbscripts.orders import exist_handler, notexist_handler
from dbscripts.delete_book import delete_handler
from menus.menus import menu_handler, admkeyboard_handler
from telegram.ext import Updater
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(menu_handler)
    dp.add_handler(admkeyboard_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(exist_handler)
    dp.add_handler(notexist_handler)
    # cюда я подтяну остальные conv-handler-ы

    """
    dp.add_handler(CommandHandler("order", get_order, pass_user_data=True))
    dp.add_handler(CommandHandler("add", get_new_books, pass_user_data=True))
    dp.add_handler(CommandHandler("change", new_description, pass_user_data=True))
    dp.add_handler(CommandHandler("sendall", send_messages))
    MessageHandler(Filters.text, get_order, pass_user_data=True)
    MessageHandler(Filters.text, get_new_books, pass_user_data=True)
    MessageHandler(Filters.text, new_description, pass_user_data=True)
    """
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()