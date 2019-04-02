import os
import local_settings as ls

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
datapath = os.path.dirname(__file__)
models = os.path.join(datapath, "bookstorebot/src/models.py")
from models import Users, Products, session
KEYBOARD, ADMIN = range(2)
def start(bot, update,user_data):
        keyboard_customer = [[InlineKeyboardButton('Список книг', callback_data='list_of_books'),
                              InlineKeyboardButton('Заказать книгу', callback_data='order_book')]]
        reply_customer = InlineKeyboardMarkup(keyboard_customer)
        update.message.reply_text('Здравствуйте! Это бот магазина "Bookstore", чем я могу помочь?',
                                  reply_markup=reply_customer)
        user_data['user_id'] = update.message.from_user.id
        user_data['username'] = update.message.from_user.name
        users = session.query(Users).all()
        for user in users:
            indata = session.query(Users).filter(Users.user_id == user_data['user_id'])
            if not indata:
                session.add(Users(user_id=user_data['user_id'], name=user_data['username']))
                session.commit()
                del user_data['user_id']
                del user_data['username']
            else:
                print('Этот пользователь уже сущ. в БД!')
                del user_data['user_id']
                del user_data['username']
                break
        return KEYBOARD
def keyboard_functions(bot, update, user_data):
        query = update.callback_query
        user_data['button'] = query.data
        books = session.query(Products)
        if user_data['button'] == 'list_of_books':
            bot.send_message(
                text='Список книг, которые есть в наличии.'
                     ' Следите за уведомлениями, возможно у нас появятся новые книги ;) ',
                chat_id=query.message.chat_id, message_id=query.message.message_id)
            for book in books:
                book_name = book.prod_name
                description = book.about
                price = str(book.cost)
                editions = str(book.edition)

                bot.send_message(text='Название:{}'.format(book_name)+' Описание:{}'.format(description) + ' Цена (в $):{}'.format(price)+' Кол-во:{}'.format(editions), chat_id=query.message.chat_id,
                                 message_id=query.message.message_id)

        elif user_data['button'] == 'Order book':
            bot.send_message(text='Хорошо, тогда введите  своё имя,'
                                  'название книги, /order e-mail,'
                                  'моб. телефон', chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
        elif user_data['button'] == 'add':
            bot.send_message(text='Окей,вот список добавленных ранее книг', chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
            for book in books:
                book_name = book.prod_name
                description = book.about
                price = str(book.cost)
                editions = str(book.edition)
                bot.send_message(text='Название:{}'.format(book_name) + ' Описание:{}'.format(description) + ' Цена (в $):{}'.format(price) + ' Кол-во:{}'.format(editions), chat_id=query.message.chat_id,message_id=query.message.message_id)
        elif user_data['button'] == 'change':
            bot.send_message(text='Введи /change название книги /change новое описание',
                             chat_id=query.message.chat_id, message_id=query.message.message_id)
        elif user_data['button'] == 'delete':
            bot.send_message(text='Введи /delete название книги ,которую ты хочешь удалить',
                             chat_id=query.message.chat_id, message_id=query.message.message_id)
        elif user_data['button'] == 'send_to_customers':
            bot.send_message(text='Окей, введи /sendall для проведения рассылки!', chat_id=query.message.chat_id,
                             message_id=query.message.message_id)
        return KEYBOARD

def get_adm(bot, update, user_data):
        text = update.message.text.replace('/admin', '')
        text = "".join(text.split())
        user_data['password'] = text
        if user_data['password'] == ls.password:
            bot.send_message(chat_id=update.message.chat_id, text='Привет, aдмин!')
            keyboard_admin = [[InlineKeyboardButton('Добавить новый товар', callback_data='add'),
                               InlineKeyboardButton('Изменить описание товара', callback_data='change')],
                              [InlineKeyboardButton('Удалить товар', callback_data='delete'),
                               InlineKeyboardButton('Провести рассылку', callback_data='send_to_customers')]]
            reply_markup = InlineKeyboardMarkup(keyboard_admin)
            update.message.reply_text('Список функций, доступных для администратора бота:', reply_markup=reply_markup)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Ошибка! Пароль введен неверно, попробуйте снова.')
        return KEYBOARD
menus_handler = ConversationHandler(  entry_points= [CommandHandler('start', start, pass_user_data=True)],
                                    states= {
                                        KEYBOARD: [CallbackQueryHandler(keyboard_functions, pass_user_data=True),
                                                   CommandHandler("admin", get_adm, pass_user_data=True)]
                                    },
                                    fallbacks=[])
