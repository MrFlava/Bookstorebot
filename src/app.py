from orders.orders import Orders
from menus.menus import Menus
from local_settings import Token, password
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
updater = Updater(Token)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", Menus.start))
dp.add_handler(CommandHandler("admin", Menus.get_adm, pass_user_data= True))
dp.add_handler(CallbackQueryHandler(Menus.keyboard_functions, pass_user_data=True))
dp.add_handler(CommandHandler('order', Orders.get_order, pass_user_data=True))
updater.start_polling()
updater.idle()
