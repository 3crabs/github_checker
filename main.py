import json
import re
import requests
import telebot


def check_url(url: str):
    return re.fullmatch(r'https://github.com/.+', url.strip())


def create_answer(url: str):
    if not check_url(url):
        return 'Ссылка некорректна. Попробуй другую.'
    else:
        response = requests.post('https://quex.tech/api/employee/repository/analyze/before',
                                 json={
                                     "locale": "ru",
                                     "repository_url": "https://github.com/git"
                                 })
        json_string = json.loads(response.text)
        if json_string['success']:
            url = json_string['data']['sign_up_url']
            return 'Чтобы получить результаты анализа, пройди по ссылке ' + url + ' Спасибо за интерес!'
        else:
            return 'Что то пошло не так. Попробуй позже.'


with open('bot.json', 'r') as file:
    data = file.read()
obj = json.loads(data)
bot = telebot.TeleBot(obj['token'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет! Я могу проанализировать твой исходный код в GitHub на наличие ошибок и уязвимостей, '
                     'и я присвою ему рейтинг на основании миллионов проанализированных репозиториев!\n'
                     'Введи ссылку на твой открытый репозиторий (Пример: https://github.com/...)',
                     disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(chat_id=message.chat.id, text=create_answer(message.text))


bot.polling()
