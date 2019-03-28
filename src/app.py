from send_to_users import send_messages
from local_settings import Token
from orders.orders import  get_order
from dbscripts.add_book import  get_new_books
from dbscripts.change_desc import  new_description
from dbscripts.delete_book import  delete_book
from menus.menus import start, keyboard_functions, get_adm
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
updater = Updater(Token)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start,pass_user_data=True))
dp.add_handler(CommandHandler("admin", get_adm, pass_user_data=True))
dp.add_handler(CommandHandler("order", get_order))
dp.add_handler(CommandHandler("add", get_new_books, pass_user_data=True))
dp.add_handler(CommandHandler("change", new_description, pass_user_data= True))
dp.add_handler(CommandHandler("delete", delete_book, pass_user_data= True))
dp.add_handler(CommandHandler("sendall", send_messages))
dp.add_handler(CallbackQueryHandler(keyboard_functions, pass_user_data=True))
MessageHandler(Filters.text, get_new_books, pass_user_data=True)
MessageHandler(Filters.text, new_description, pass_user_data= True)
updater.start_polling()
updater.idle()
