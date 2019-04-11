from src.models import Users, session
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
SEND_MESSAGE = range(1)
def message_instruction(bot,update):
    bot.send_message(text='Окей, введи текст для рассылки', chat_id=update.message.chat_id,
                     message_id=update.message.message_id)
    return SEND_MESSAGE
def send_messages(bot,update):
    text = update.message.text
    users = session.query(Users)
    for user in users:
        user = user.user_id
        bot.send_message(chat_id=user, text = text)
    bot.send_message(text='Рассылка произведена!', chat_id=update.message.chat_id,
                     message_id=update.message.message_id)
    return SEND_MESSAGE

sends_handler = ConversationHandler(entry_points=[CommandHandler("sendall", message_instruction)],
                                     states={
                                         SEND_MESSAGE: [MessageHandler(Filters.text, send_messages)]},
                                     fallbacks=[])