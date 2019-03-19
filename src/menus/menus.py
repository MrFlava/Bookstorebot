import local_settings as ls
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Menus():

    def start(bot, update):
        keyboard_customer = [[InlineKeyboardButton('Список книг', callback_data= 'List of books'),InlineKeyboardButton('Заказать книгу', callback_data= 'Order book')]]
        reply_customer = InlineKeyboardMarkup(keyboard_customer)
        update.message.reply_text('Здравствуйте! Это бот магазина "Bookstore", чем я могу помочь?', reply_markup = reply_customer)

    def keyboard_functions(bot, update, user_data):
        query = update.callback_query
        user_data['button'] = query.data
        db = ls.connect
        books = db.execute("SELECT title , description , price FROM books")
        if user_data['button'] == 'List of books':
            bot.send_message(text= 'Список книг, которые есть в наличии. Следите за уведомлениями, возможно у нас появятся новые книги ;) ', chat_id = query.message.chat_id, message_id= query.message.message_id)
            bot.send_message(text= 'Название   Описание   Цена', chat_id = query.message.chat_id, message_id= query.message.message_id)
            for  i in books:
                book = str(i)
                book = book.replace('(','')
                book = book.replace(')','')
                bot.send_message(text = book, chat_id = query.message.chat_id, message_id= query.message.message_id)
        elif user_data['button'] == 'Order book':
            bot.send_message(text= 'Хорошо, тогда введите /order', chat_id = query.message.chat_id, message_id= query.message.message_id)
        elif user_data['button'] == 'Add':
            bot.send_message(text= 'Окей,заполни форму', chat_id = query.message.chat_id, message_id= query.message.message_id)
        elif user_data['button'] == 'Change':
            bot.send_message(text= 'Введи номер(/id номер) книги,описание которой ты хочешь поменять', chat_id = query.message.chat_id, message_id= query.message.message_id)
        elif user_data['button'] == 'Delete':
            bot.send_message(text= 'Введи номер(/id номер) книги которую ты хочешь удалить', chat_id = query.message.chat_id, message_id= query.message.message_id)
        elif user_data['button'] == 'Send to customers':
            bot.send_message(text= 'Рассылка произведена!', chat_id = query.message.chat_id, message_id= query.message.message_id)

    def get_adm(bot, update, user_data):
        text = update.message.text.replace('/admin','')
        text = "".join(text.split())
        user_data['password'] = text
        if user_data['password'] == ls.password:
            bot.send_message(chat_id = update.message.chat_id, text = 'Привет, aдмин!')
            keyboard_admin =[[InlineKeyboardButton('Добавить новый товар', callback_data= 'Add'), InlineKeyboardButton('Изменить описание товара', callback_data='Change')],[InlineKeyboardButton('Удалить товар', callback_data= 'Delete'), InlineKeyboardButton('Провести рассылку',callback_data='Send to customers')]]
            reply_markup = InlineKeyboardMarkup(keyboard_admin)
            update.message.reply_text('Список функций, доступных для администратора бота:',reply_markup = reply_markup)
        else:
            bot.send_message(chat_id = update.message.chat_id, text = 'Ошибка! Пароль введен неверно, попробуйте снова.')
