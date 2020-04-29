import json

import telebot

from answer import create_answer, create_hello_message

with open('bot.json', 'r') as file:
    data = file.read()
obj = json.loads(data)
bot = telebot.TeleBot(obj['token'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, create_hello_message('ru'), disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(chat_id=message.chat.id, text=create_answer(message.text, 'ru'))


bot.polling()
