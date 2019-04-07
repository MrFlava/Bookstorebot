import os
import formencode
datapath = os.path.dirname(__file__) #Уберу, как только будет setup.py
models = os.path.join(datapath, "bookstorebot/src/models.py")
from  telegram.ext import MessageHandler, ConversationHandler,RegexHandler, Filters #для ConvHandler
from models import session, Orderbooks
BOOK, BOOK_NOTEXIST = range(2)
def order_not_exist_book(bot,update):
    bot.send_message(chat_id=update.message.chat_id, message_id=update.message.message_id, text='Тогда введите: свой ник,название заказанной книги, e-mail и моб. телефон. Мы сообщим, когда она будет в наличии!')
    return BOOK_NOTEXIST
def order_exist_book(bot,update):
    bot.send_message(chat_id=update.message.chat_id, message_id=update.message.message_id, text='Отлично, тогда введите: свой ник,название книги, e-mail и моб.телефон')
    return BOOK

def record_order(bot, update,user_data):
    text = update.message.text

    if 'name' not in user_data:
        name = formencode.validators.String()
        user_data['name'] = name.to_python(text)
    elif 'book' not in user_data:
        book = formencode.validators.String()
        user_data['book'] = book.to_python(text)
    elif 'e-mail' not in user_data:
        email = formencode.validators.String()
        user_data['e-mail'] = email.to_python(text)
    elif 'phone' not in user_data:
        phonenumper =  formencode.validators.Number()
        user_data['phone'] = phonenumper.to_python(text)
        session.add(Orderbooks(nickname=user_data['name'], bookname=user_data['book'],
                               email=user_data['e-mail'], phone=user_data['phone']))
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Отлично, заказ принят! '
                                                                'О всех подробностях заказа вам будет '
                                                                'сообщать администратор бота!')
        del user_data['name']
        del user_data['book']
        del user_data['e-mail']
        del user_data['phone']
        return BOOK, BOOK_NOTEXIST

exist_handler = ConversationHandler(entry_points=[RegexHandler('Да', order_exist_book)],
                                      states={
                                          BOOK: [MessageHandler(Filters.text, record_order,pass_user_data=True)]
                                      }, fallbacks=[])

notexist_handler = ConversationHandler(entry_points=[RegexHandler('Нет', order_not_exist_book)],
                                      states={
                                          BOOK_NOTEXIST: [MessageHandler(Filters.text, record_order,pass_user_data=True)]
                                      }, fallbacks=[])
