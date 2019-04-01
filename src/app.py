from local_settings import Token
"""
from orders.orders import  get_order
from send_to_users import send_messages
from dbscripts.add_book import  get_new_books
from dbscripts.delete_book import  delete_book
from dbscripts.change_desc import  new_description
"""
from menus.menus import menus_handler
from telegram.ext import Updater
def main():
    updater = Updater(Token)
    dp = updater.dispatcher
    dp.add_handler(menus_handler)
    """
    dp.add_handler(CommandHandler("order", get_order, pass_user_data=True))
    dp.add_handler(CommandHandler("add", get_new_books, pass_user_data=True))
    dp.add_handler(CommandHandler("change", new_description, pass_user_data=True))
    dp.add_handler(CommandHandler("delete", delete_book, pass_user_data=True))
    dp.add_handler(CommandHandler("sendall", send_messages))
    MessageHandler(Filters.text, get_order, pass_user_data=True)
    MessageHandler(Filters.text, get_new_books, pass_user_data=True)
    MessageHandler(Filters.text, new_description, pass_user_data=True)
    """
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()