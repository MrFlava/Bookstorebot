from local_settings import Token
from orders.orders import  get_order
from dbscripts.add_books import  get_new_books
from dbscripts.change_desc import  new_description
from menus.menus import start, keyboard_functions, get_adm
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
updater = Updater(Token)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("admin", get_adm, pass_user_data=True))
dp.add_handler(CommandHandler("order", get_order))
dp.add_handler(CommandHandler("add", get_new_books, pass_user_data=True))
dp.add_handler(CommandHandler("change",new_description))
dp.add_handler(CallbackQueryHandler(keyboard_functions, pass_user_data=True))
MessageHandler(Filters.text, get_new_books, pass_user_data=True)
MessageHandler(Filters.text, new_description)
updater.start_polling()
updater.idle()
