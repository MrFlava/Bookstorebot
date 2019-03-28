import  sys
sys.path.append("/home/user/PycharmProjects/bookstorebot/src/models.py")
from  models import session, Orderbooks
def get_order(bot, update, user_data):
    text = update.message.text.replace("/order", "")
    text = "".join(text.split())
    if 'name' not in user_data:
        user_data['name'] = text
    elif 'book' not in user_data:
        user_data['book']  = text
    elif 'e-mail' not in user_data:
        user_data['e-mail'] = text
    elif 'phone' not in user_data:
        user_data['phone'] = int(text)
        session.add(Orderbooks(nickname=user_data['name'],bookname=user_data['book'], email=user_data['e-mail'], phone=user_data['phone']))
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Отлично, заказ принят! О всех подробностях заказа вам будет сообщать администратор бота!')
        del user_data['name']
        del user_data['book']
        del user_data['email']
        del user_data['phone']


