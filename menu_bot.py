import telebot
from config import Token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(token=Token)


# define the main menu
def main_menu():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('photos', callback_data='submenu1')
    button2 = InlineKeyboardButton('videos', callback_data='submenu2')
    markup.add(button1, button2)
    return markup


# def submenus for menu 1
def sub_menu1():  # photos menu
    markup = InlineKeyboardMarkup(row_width=2)
    button3 = InlineKeyboardButton("colored photos", callback_data="submenu1-1")
    button4 = InlineKeyboardButton("b-w photos", callback_data="submenu1-2")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_main")
    markup.add(button3, button4, return_button)
    return markup


def sub_menu1_1():  # colored
    markup = InlineKeyboardMarkup(row_width=2)
    button6 = InlineKeyboardButton("ashley era", callback_data="ashley")
    button5 = InlineKeyboardButton("halsey era", callback_data="halsey")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_submenu1")
    markup.add(button5, button6, return_button)
    return markup


def sub_menu1_2():  # black-white
    markup = InlineKeyboardMarkup(row_width=2)
    button7 = InlineKeyboardButton("ashley era", callback_data="ashley")
    button8 = InlineKeyboardButton("halsey era", callback_data="halsey")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_submenu1")
    markup.add(button7, button8, return_button)
    return markup


# def sub menus for menu 2 ---------------------------------------------

def sub_menu2():  # videos menu
    markup = InlineKeyboardMarkup(row_width=2)
    button3 = InlineKeyboardButton("live", callback_data="submenu2-1")
    button4 = InlineKeyboardButton("MV", callback_data="submenu2-2")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_main")
    markup.add(button3, button4, return_button)
    return markup


def sub_menu2_1():  # live
    markup = InlineKeyboardMarkup(row_width=2)
    button7 = InlineKeyboardButton("ashley era", callback_data="ashley")
    button8 = InlineKeyboardButton("halsey era", callback_data="halsey")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_submenu2")
    markup.add(button7, button8, return_button)
    return markup


def sub_menu2_2():
    markup = InlineKeyboardMarkup(row_width=2)
    button7 = InlineKeyboardButton("ashley era", callback_data="ashley")
    button8 = InlineKeyboardButton("halsey era", callback_data="halsey")
    return_button = InlineKeyboardButton("go back", callback_data="return_to_submenu2")
    markup.add(button7, button8, return_button)
    return markup


# start command handler
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, text="welcome to my era!")
    bot.send_message(message.chat.id, text="you are in the main menu, choose an option", reply_markup=main_menu())


# callback query handler
@bot.callback_query_handler(func=lambda call: True)
# برای تشخیص (خوندن) پیامی که بعد از انتخاب یکی از گزینه های منیو به تلگرم ارسال میشه
def callback_query(call):
    if call.data == 'submenu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="choose colored or black and white:", reply_markup=sub_menu1())

    elif call.data == "submenu1-1":  # colored a/h
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="😭(c)", reply_markup=sub_menu1_1())

    elif call.data == "submenu1-2":  # b-w a/h
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="😭(bw)", reply_markup=sub_menu1_2())

    elif call.data == "halsey":
        pass

    elif call.data == "ashley":
        pass

    # sub 2 ------------------------
    elif call.data == 'submenu2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="choose live or music video", reply_markup=sub_menu2())

    elif call.data == 'submenu2-1':  # live a/h
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="😭😭(l):", reply_markup=sub_menu2_1())

    elif call.data == "submenu2-2":  # mv a/h
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="😭😭(mv)", reply_markup=sub_menu2_2())

    elif call.data == "halsey":
        pass

    elif call.data == "ashley":
        pass

    # return buttons --------------- sub 1
    elif call.data == "return_to_main":  # sub1 --> main
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="tell me photos or videos? ", reply_markup=main_menu())

    elif call.data == "return_to_submenu1":  # sub1-1 --> sub1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="choose colored or black and white:", reply_markup=sub_menu1())

    elif call.data == "return_to_submenu1":  # sub1-2 --> sub1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="choose colored or black and white:", reply_markup=sub_menu1())

    # return buttons --------------- sub 2
    elif call.data == "return_to_main":  # sub2 --> main
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="tell me photos or videos?", reply_markup=main_menu())

    elif call.data == "return_to_submenu2":  # sub1-1 --> sub1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="live menu", reply_markup=sub_menu2())

    elif call.data == "return_to_submenu2":  # sub1-2 --> sub1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="music videos", reply_markup=sub_menu2())


print("Bot is running...")
bot.polling()
