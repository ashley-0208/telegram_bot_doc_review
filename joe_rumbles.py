import telebot
import logging

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot('7463771495:AAGZrXOrp_z5QFQqvsgEHXhEkNegZTaWq5g')


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to hell:))")
    bot.reply_to(message, "reply?")


print("Bot is running...")
bot.polling()
