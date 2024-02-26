import telebot
import time
from telebot import types

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = '7125958977:AAHMRgilpAgJ1kINLXk4A7OUcWfPkB_ZGZ4'

# Замените список 'TARGET_PHRASES' на вариации словосочетаний, которые вы хотите проверять в сообщениях
TARGET_PHRASES = ['@vozmishev', ':@vozmishev', ': @vozmishev', '@gifesttt', ':@gifesttt', ': @gifesttt']

admin_id = 753113351
moder1_id = 925051239
moder2_id = 789022369

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def check_message(message):
    chat_id = message.chat.id
    message_text = message.text.lower()
    user_id = message.from_user.id
    if not any(phrase in message_text for phrase in TARGET_PHRASES) and user_id not in [admin_id, moder1_id, moder2_id]:
        # Удаляем сообщение
        bot.delete_message(chat_id, message.message_id)
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        bot_msg = f"⚠️ {mention}, составьте сообщение по форме, с указанием тега гаранта: @vozmishev или @gifesttt "
        sent_message = bot.send_message(message.chat.id, bot_msg, parse_mode="Markdown")
        time.sleep(15)
        bot.delete_message(message.chat.id, sent_message.message_id)



if __name__ == "__main__":
    bot.polling(none_stop=True)