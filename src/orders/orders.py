import local_settings as ls
class Orders():
    def get_order(bot,update, user_data):
        bot.send_message(text = 'Хорошо, введите название выбранной книги', chat_id = update.message.chat_id, message_id = update.message.message_id)
