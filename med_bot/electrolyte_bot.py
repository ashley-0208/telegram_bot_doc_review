import telebot
from config import token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(Token=token)

# define buttons:
button1 = InlineKeyboardButton(text="علائم")


@bot.message_handler(commands=['start'])
def start_msg(msg):
    bot.message_handler(msg.chat.id, 'welcom to the bot', reply_markup=None)

