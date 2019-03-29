import  os
datapath = os.path.dirname(__file__)
models =os.path.join(datapath, "bookstorebot/src/models.py")
from models import  Products, session
def delete_book(bot,update,user_data):
    text = update.message.text.replace("/delete", "")
    text = "".join(text.split())
    if 'deleted_book' not in user_data:
        user_data['deleted_book'] = text
        query = session.query(Products).filter(Products.prod_name == user_data['deleted_book']).delete()
        session.commit()
        bot.send_message(chat_id=update.effective_user.id, text='Данные товара успешно удалены!')
        del user_data['deleted_book']
