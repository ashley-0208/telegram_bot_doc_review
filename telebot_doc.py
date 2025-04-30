import telebot
from config import Token

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to my era:))")
    # bot.reply_to(message, "reply?")
    bot.send_message(message.chat.id, "please enter your name.")
    bot.register_next_step_handler(message, process_name)


def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Hello {name}, How old are you')

    bot.register_next_step_handler(message, process_age)


def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f'You are {age}. \nThank you.')


@bot.message_handler(content_types=["help"])
def handle_start_help(message):
    bot.send_message(message.chat.id, "How can i help you!")


@bot.message_handler(content_types=["document", "audio"])
def handle_doc_audio(message):
    if message.audio:
        bot.reply_to(message, "this is an audio.")
    elif message.document:
        bot.reply_to(message, "this is a doc.")


@bot.message_handler(regexp="2025")
def handle_regexp(message):
    bot.reply_to(message, "this message contains 2025")


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=["document"])
def handle_text_lamda(message):
    bot.reply_to(message, "this is a text file")


# برای اجرا شدن این کامند باید تابع handle doc audio غیرفعال بشه!


def text_test(message):
    return message.document.mime_type == "text/plain"


# works like lambda

@bot.message_handler(func=text_test, content_types=["document"])
def handle_text_func(message):
    bot.reply_to(message, "text file with func")


@bot.message_handler(commands=["hello"])  # or...
@bot.message_handler(func=lambda msg: msg.text == "😂")
def send_smth(message):
    bot.reply_to(message, 'Emoji')


user_ID = []


@bot.message_handler(commands=["SUPU2025"])  # send user product update
def send_updates(message):
    if message.chat.id not in user_ID:
        user_ID.append(message.chat.id)  # this if statement is better to be writen in "welcome" message handler!
    for ID in user_ID:
        bot.send_message(ID, "the product is available")


print("bot is running...")
bot.polling()
