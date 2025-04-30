import telebot
from config import Token

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to hell:))")
    bot.reply_to(message, "reply?")


print("Bot is running...")
bot.polling()
