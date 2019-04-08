import formencode
from src.models import Products, session
from  telegram.ext import  ConversationHandler, CommandHandler, MessageHandler, Filters
RECORD_BOOKS = range(1)
def new_books_instruction(bot, update):
    bot.send_message(chat_id = update.message.chat_id, message_id = update.message.message_id,
                     text='Введи: id-книги, название книги, описание книги, цену и кол-во экземпляров')
    return RECORD_BOOKS
def record_new_books(bot, update,user_data):
    text = update.message.text
    if 'book_id' not in user_data:
        id = formencode.validators.Number()
        user_data['book_id'] = id.to_python(text)
    if 'title' not in user_data:
        title = formencode.validators.String()
        user_data['title'] = title.to_python(text)
    elif 'description' not in user_data:
        description = formencode.validators.String()
        user_data['description'] = description.to_python(text)
    elif 'price' not in user_data:
        price = formencode.validators.Number()
        user_data['price'] = price.to_python(text)
    elif 'examples' not in user_data:
        examples = formencode.validators.Number()
        user_data['examples'] = examples.to_python(text)
        session.add(Products(id_book=user_data['book_id'], prod_name=user_data['title'],
                             about=user_data['description'], cost=user_data['price'], edition=user_data['examples']))
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Отлично, данные успешно записаны!')
        del user_data['book_id']
        del user_data['title']
        del user_data['description']
        del user_data['price']
        del user_data['examples']
        return RECORD_BOOKS
record_handler = ConversationHandler(entry_points=[CommandHandler("add", new_books_instruction)],
                                     states={
                                         RECORD_BOOKS: [MessageHandler(Filters.text, record_new_books, pass_user_data=True)]},
                                     fallbacks=[])
