import enum
from botmanlib.menus.basemenu import BaseMenu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from src.models import Users, Products, session


class StartMenu(BaseMenu):
    class States(enum.Enum):
        KEYBOARD = 1
    def start(self, bot, update, user_data):
        keyboard_customer = [[InlineKeyboardButton('Список книг', callback_data='list_of_books'),
                              InlineKeyboardButton('Заказать книгу', callback_data='order_book')]]
        reply_customer = InlineKeyboardMarkup(keyboard_customer)
        update.message.reply_text('Вас приветствует бота магаизина "Bookstore". Чем могу быть полезен?', reply_markup=reply_customer)
        user_data['user_id'] = update.message.from_user.id
        user_data['username'] = update.message.from_user.name
        users = session.query(Users).all()
        for user in users:
            indata = session.query(Users).filter(Users.user_id == user_data['user_id']) #мало данных
            if not indata:
                session.add(Users(user_id=user_data['user_id'], name=user_data['username']))
                session.commit()
            else:
                print('Этот пользователь уже сущ. в БД!')
                break
        return self.States.KEYBOARD

    def user_keyboard_functions(self, bot, update, user_data):
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

                bot.send_message(
                    text='Название:{}'.format(book_name) + ' Описание:{}'.format(description) + ' Цена (в $):{}'.format(
                        price) + ' Кол-во:{}'.format(editions), chat_id=query.message.chat_id,
                    message_id=query.message.message_id)
        elif user_data['button'] == 'order_book':
            kb = [[KeyboardButton('Да')], [KeyboardButton('Нет')]]
            kb_markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True, resize_keyboard=True)
            bot.send_message(text='Вы точно нашли подходящюю для вас книгу?', chat_id=query.message.chat_id,
                             message_id=query.message.message_id, reply_markup=kb_markup)
        return self.States.KEYBOARD

    def get_handler(self):
        handler = ConversationHandler(entry_points=[CommandHandler('start', self.start, pass_user_data=True)],
                                           states={
                                               self.States.KEYBOARD: [
                                                   CallbackQueryHandler(self.user_keyboard_functions, pass_user_data=True)]},
                                           fallbacks=[]) #Полюбому должны быть!
        return handler
