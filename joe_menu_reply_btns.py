import telebot
from config import Token
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot(Token)

# creating the reply keyboard
rep_key = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
# resize: changes keyboard size according to users screen! // onetime: use menu more than once
rep_key.add("button1", "button2")


# handling ths /start command
@bot.message_handler(commands=["start"])
def wellcome(message):
    bot.reply_to(message=message, text="check the following keyboard", reply_markup=rep_key)


# handling all other messages
@bot.message_handler(func=lambda message: True)
def check_button(message):
    if message.text == "button1":
        bot.reply_to(message, "😂")
    elif message.text == "button2":
        bot.reply_to(message, "😭")
    else:
        bot.reply_to(message, f"your message is: {message.text}")


print("Bot is running...")
bot.polling()
