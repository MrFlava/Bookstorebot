import  sys
sys.path.append("/home/user/PycharmProjects/bookstorebot/src/models.py")
from models import Books, session
def get_new_books(bot, update, user_data):
    text = update.message.text.replace("/add", " ")
    text = "".join(text.split())
    if 'Title' not in user_data:
        user_data['Title'] = text
    elif 'Description' not in user_data:
        user_data['Description'] = text
    elif 'Price' not in user_data:
        user_data['Price'] = text
        session.add(Books(title = user_data['title'],description =  user_data['description'], price =  user_data['price']))
        session.commit()
        bot.send_message(chat_id = update.effective_user.id, text = 'Отлично, данные успешно записаны!')
        del user_data['Title']
        del user_data['Description']
        del user_data['Price']
