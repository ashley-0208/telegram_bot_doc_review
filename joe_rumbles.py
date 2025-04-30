import telebot
from config import Token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(Token)

# defining and adding buttons
button1 = InlineKeyboardButton(text="google", url="https://google.com")
button2 = InlineKeyboardButton(text="Github", url="https://github.com")
button3 = InlineKeyboardButton(text="callback1", callback_data="stop tapping man")
button4 = InlineKeyboardButton(text="callback2", callback_data="bro u are sick!")
inline_keyboard = InlineKeyboardMarkup(row_width=2)  # هر سطری که بالا میاد 2 دکمه باشه
inline_keyboard.add(button1, button2, button3, button4)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to my era:))", reply_markup=inline_keyboard)

# callback query handler for inline keyboard buttons


@bot.callback_query_handler(func=lambda call: True)
def check_button(call):
    if call.data == "btn1":
        bot.answer_callback_query(call.id, "btn1 is tapped!", show_alert=True)
    elif call.data == "btn2":
        bot.answer_callback_query(call.id, "btn2 is tapped!")


print("Bot is running...")
bot.polling()
