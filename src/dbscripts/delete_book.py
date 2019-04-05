import os
import formencode
datapath = os.path.dirname(__file__)#Уберу, как только будет setup.py
models =os.path.join(datapath, "bookstorebot/src/models.py")
from  telegram.ext import  MessageHandler,ConversationHandler, CommandHandler, Filters
from models import  Products, session
DELETE = range(1)
def delete_book(bot,update,user_data):
    text = update.message.text.replace("/delete", "")
    text = "".join(text.split())
    if 'deleted_book' not in user_data:
        book = formencode.validators.String()
        user_data['deleted_book'] = book.to_python(text)
        query = session.query(Products).filter(Products.prod_name == user_data['deleted_book']).delete()
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Данные товара успешно удалены!')
        del user_data['deleted_book']
    return DELETE

delete_handler = ConversationHandler( entry_points=[CommandHandler('delete', delete_book, pass_user_data=True)],
                                      states={
                                          DELETE: [MessageHandler(Filters.text, delete_book, pass_user_data=True)]
                                      },
                                      fallbacks=[])