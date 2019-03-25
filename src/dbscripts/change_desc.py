import  sys
sys.path.append("/home/user/PycharmProjects/bookstorebot/src/models.py")
from models import  Books, session


def new_description(bot,update, user_data):
    text = update.message.text.replace("/change", " ")
    text = "".join(text.split())
    if 'title' not in user_data:
        user_data['title'] = text
    elif 'new_description' not in user_data:
        user_data['new_description'] = text
        query = session.query(Books).filter(Books.title == user_data['title']).\
            update({Books.description: user_data['new_description']}, synchronize_session=False)
        session.commit()
        bot.send_message(chat_id=update.message.chat_id, message_id=update.message.message_id,
                         text='Описание изменено!')
        del user_data['new_description']
        del user_data['title']

    """
    book3.description = user_data['new_description']
    session.add(book3)

    session.commit()
"""