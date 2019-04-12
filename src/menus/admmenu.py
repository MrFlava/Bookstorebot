import enum
from src.settings import ADMIN_PASSWORD
from botmanlib.menus.basemenu import BaseMenu
from src.models import Products, session
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Admmenu(BaseMenu):
    class States(enum.Enum):
        ADMKEYBOARD = 1

    def admkeyboard_functions(self, bot, update, user_data):
            query = update.callback_query
            user_data['adm_button'] = query.data
            books = session.query(Products)
            if user_data['adm_button'] == 'add':
                bot.send_message(text='Окей,вот список добавленных ранее книг', chat_id=query.message.chat_id,
                                 message_id=query.message.message_id)
                for book in books:
                    book_name = book.prod_name
                    description = book.about
                    price = str(book.cost)
                    editions = str(book.edition)
                    bot.send_message(
                        text='Название:{}'.format(book_name) + ' Описание:{}'.format(
                            description) + ' Цена (в $):{}'.format(
                            price) + ' Кол-во:{}'.format(editions), chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
                    bot.send_message(tex='Для добавления новой книги введи /add и следуй дальнейшим инструкциям',
                                     chat_id=query.message.chat_id, message_id=query.message.message_id)
            elif user_data['adm_button'] == 'change':
                bot.send_message(text='Введи /change название книги /change новое описание',
                                 chat_id=query.message.chat_id, message_id=query.message.message_id)
            elif user_data['adm_button'] == 'delete':
                bot.send_message(text='Введи /delete название книги ,которую ты хочешь удалить',
                                 chat_id=query.message.chat_id, message_id=query.message.message_id)
            elif user_data['adm_button'] == 'send_to_customers':
                bot.send_message(text='Окей, введи /sendall для проведения рассылки!', chat_id=query.message.chat_id,
                                 message_id=query.message.message_id)
            return self.States.ADMKEYBOARD
    def get_adm(self, bot, update, user_data):
            text = update.message.text.replace('/admin', '')
            text = "".join(text.split())
            user_data['password'] = text
            if user_data['password'] == ADMIN_PASSWORD:
                bot.send_message(chat_id=update.message.chat_id, text='Привет, aдмин!')
                keyboard_admin = [[InlineKeyboardButton('Добавить новый товар', callback_data='add'),
                                   InlineKeyboardButton('Изменить описание товара', callback_data='change')],
                                  [InlineKeyboardButton('Удалить товар', callback_data='delete'),
                                   InlineKeyboardButton('Провести рассылку', callback_data='send_to_customers')]]
                reply_markup = InlineKeyboardMarkup(keyboard_admin)
                update.message.reply_text('Список функций, доступных для администратора бота:',
                                          reply_markup=reply_markup)
            else:
                bot.send_message(chat_id=update.message.chat_id,
                                 text='Ошибка! Пароль введен неверно, попробуйте снова.')
            return self.States.ADMKEYBOARD

    def get_handler(self):
            handler = ConversationHandler(
                entry_points=[CommandHandler('admin', self.get_adm, pass_user_data=True)],
                states={
                    self.States.ADMKEYBOARD: [CallbackQueryHandler(self.admkeyboard_functions,
                                                                   pass_user_data=True)]},
                fallbacks=[])
            return handler