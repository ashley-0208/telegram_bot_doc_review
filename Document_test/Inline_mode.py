import telebot
from config import Token
from telebot.types import Audio as au, InlineKeyboardButton, InlineKeyboardMarkup, CopyTextButton

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'copy'])
def welcome(message):
    # bot.reply_to(message.chat.id, 'welcome')
    markup = InlineKeyboardMarkup()
    # button = InlineKeyboardButton(text='Click me!', callback_data='button_click')
    copy = CopyTextButton(text='this is the text to copy!', callback_data='copy')
    button2 = InlineKeyboardButton(text='', switch_inline_query=copy.text)
    markup.add(button2)

    # bot.send_message(message.chat.id, 'please click on button!', reply_markup=markup)
    bot.send_message(message.chat.id, 'click the button below to copy the text', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'button_click':
        bot.answer_callback_query(call.id, text='you clicked the button')
        bot.send_message(call.message.chat.id, 'thanks for clicking!')


@bot.message_handler(commands=['members'])
def list_members(message):
    chat_id = message.chat.id
    members = bot.get_chat_administrators(chat_id)
    response = ''
    for member in members:
        user = member.user
        status = member.status
        response += f'User: {user.first_name} {user.last_name} or " " (status:{status})\n'

        bot.send_message(chat_id, response)





@bot.message_handler(content_types=['audio'])
def file_id_handler(message):
    file_id = message.audio.file_id
    unique_id = message.audio.file_unique_id
    return file_id, unique_id


audio = au(
    file_id=file_id_handler,
    file_unique_id=file_id_handler,
    duration=120)

print('bot is running')
bot.polling()
