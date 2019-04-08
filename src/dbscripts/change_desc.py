from telegram.ext import  MessageHandler, Filters, ConversationHandler, CommandHandler
datapath = os.path.dirname(__file__)
from src.models import Products, session
NEW_DESC = range(1)
def change_instruction(bot,update):
    bot.send_message(text='Введи название книги и новое описание',
                     chat_id=update.message.chat_id, message_id=update.message.message_id)
    return  NEW_DESC
def change_desc(bot,update,user_data):
    text = update.message.text
    if 'title' not in user_data:
        user_data['title'] = text
    elif 'new_description' not in user_data:
        user_data['new_description'] = text
        query = session.query(Products).filter(Products.prod_name == user_data['title']).\
            update({Products.about: user_data['new_description']}, synchronize_session=False)
        session.commit()
        bot.send_message(chat_id=update.message.chat_id, message_id=update.message.message_id,
                         text='Описание изменено!')
        del user_data['new_description']
        del user_data['title']
        return NEW_DESC
    
desc_handler = ConversationHandler(  entry_points= [CommandHandler('change', change_instruction)],
                                    states= {
                                        NEW_DESC: [MessageHandler(Filters.text, change_desc, pass_user_data=True)]},
                                    fallbacks=[])
