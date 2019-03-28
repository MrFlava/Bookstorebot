import sys
sys.path.append("/home/user/PycharmProjects/bookstorebot/src/models.py")
from  models import Users,session
def send_messages(bot,update):
    users = session.query(Users)
    for user in users:
        user  = user.user_id
        bot.send_message(chat_id=user, text="Хэй, хэй, хээй, завезли новые книги!")
    bot.send_message(text='Рассылка произведена!', chat_id=update.message.chat_id,
                         message_id=update.message.message_id)
