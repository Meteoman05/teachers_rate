import telebot as tb
from telebot.types import (InlineKeyboardMarkup as kbi,
                           InlineKeyboardButton as bt,
                           ReplyKeyboardRemove as delete)

from config import TOKEN
from keyboard import kbc

bot = tb.TeleBot(TOKEN, num_threads=5) 

@bot.message_handler(commands=['start'])
def start(msg):
	#bot.get_chat_member(msg.chat.id, 1056861912))
	kb = kbc([('1', 'one'), ('2', 'two')])
	MSG = bot.send_message(msg.chat.id, f't', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data == 'one')
def handler(call):
	print(call.data)


@bot.callback_query_handler(func=lambda call: call.data == 'two')
def handler(call):
	bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text, message_id= call.message.id, reply_markup=kbi())
	print(call.from_user.id)

bot.polling(none_stop=True)
