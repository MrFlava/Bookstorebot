import  os
datapath = os.path.dirname(__file__)
models =os.path.join(datapath, "bookstorebot/src/models.py")
from models import Products, session

def get_new_books(bot, update, user_data):
    text = update.message.text.replace("/add", "")
    text = "".join(text.split())
    if 'book_id' not in user_data:
        user_data['book_id'] = int(text)
    if 'title' not in user_data:
        user_data['title'] = text
    elif 'description' not in user_data:
        user_data['description'] = text
    elif 'price' not in user_data:
        user_data['price'] = int(text)
    elif 'examples' not in user_data:
        user_data['examples'] = int(text)
        session.add(Products(id_book=user_data['book_id'], prod_name=user_data['title'], about=user_data['description'], cost=user_data['price'], edition=user_data['examples']))
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Отлично, данные успешно записаны!')
        del user_data['book_id']
        del user_data['title']
        del user_data['description']
        del user_data['price']
        del user_data['examples']
