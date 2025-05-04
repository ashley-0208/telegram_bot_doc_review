import telebot
from config import Token

bot = telebot.TeleBot(token=Token)


@bot.message_handler(content_types=["new_chat_members"])
def welcome_to_group(message):
    for new_member in message.new_chat_members:
        welcome_text = f"Hi {message.from_user.first_name}, Welcome to the group"
        bot.send_message(message.chat.id, text=welcome_text)


def is_admin(chat_id, user_id):
    admins = bot.get_chat_administrators(chat_id)
    for admin in admins:
        if admin.user.id == user_id:
            return True
    return False


@bot.message_handler(func=lambda message: message.text == "pin")
def pin_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if is_admin(chat_id, user_id):
        if message.reply_to_message:
            bot.pin_chat_message(chat_id, message.reply_to_message.message_id)
            bot.reply_to(message.reply_to_message, "the message is pinned")
        else:
            bot.reply_to(message, "please reply to message you want to pin")
    else:
        bot.reply_to(message.chat.id, "only admins can pin messages")


print("Bot is running...")
bot.polling()
