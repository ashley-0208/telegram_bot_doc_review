# connecting bot to database
from config import Token
from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3

# create the bot
bot = TeleBot(token=Token)

# create the keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button = KeyboardButton(text="send my info", request_contact=True)
keyboard.add(button)

# create the database
with sqlite3.connect("user.db") as conn:
    cursor = conn.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users(
            id integer primary key,
            first_name text,
            last_name text,
            phone_number text
        );
    '''
cursor.execute(create_table_query)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, text="welcome to my era!", reply_markup=keyboard)


@bot.message_handler(content_types=["contact"])
def contact(message):
    # bot.send_message(message.chat.id, text=f"{message.contact}")
    with sqlite3.connect("user.db") as conn:
        cursor = conn.cursor()
        insert_data_query = '''
            INSERT INTO users(id, first_name, last_name, phone_number)
            VALUES (?,?,?,?)
        '''
        data = (
            message.contact.user_id,
            f"{message.contact.first_name}",
            f"{message.contact.last_name}",
            f"{message.contact.phone_number}"
        )
        cursor.execute(insert_data_query, data)  # sql (str) – A single SQL statement
        #  // sql (str) – A single SQL statement - Python values to bind to placeholders in sql


print("bot is running...")
bot.polling()
