import json
import re

import requests


def check_url(url: str):
    return re.fullmatch(r'https://github.com/.+', url.strip())


def create_answer(url: str, language: str):
    if not check_url(url):
        return create_invalid_link_message(language)
    else:
        response = requests.post('https://quex.tech/api/employee/repository/analyze/before',
                                 json={
                                     "locale": "ru",
                                     "repository_url": "https://github.com/git"
                                 })
        json_string = json.loads(response.text)
        if json_string['success']:
            url = json_string['data']['sign_up_url']
            return create_link_message(url, language)
        else:
            return create_wrong_message(language)


def create_hello_message(language: str):
    if language == 'ru':
        return 'Привет! Я могу проанализировать твой исходный код в GitHub на наличие ошибок и уязвимостей, ' \
               'и я присвою ему рейтинг на основании миллионов проанализированных репозиториев!\n' \
               'Введи ссылку на твой открытый репозиторий (Пример: https://github.com/...)'
    else:
        return "Hello! I can analyze your source code on github and find mistakes and vulnerabilities of it." \
               "After that I’ll assign it's rating based on millions of analyzed repositories.\n" \
               "Enter a link to your public repository (Example: https://github.com/...)"


def create_invalid_link_message(language: str):
    if language == 'ru':
        return 'Ссылка некорректна. Попробуй другую.'
    else:
        return 'The link is invalid. Try another one.'


def create_wrong_message(language: str):
    if language == 'ru':
        return 'Что то пошло не так. Попробуй позже.'
    else:
        return 'Something went wrong. Try again later.'


def create_link_message(url: str, language: str):
    if language == 'ru':
        return 'Чтобы получить результаты анализа, пройди по ссылке ' + url + ' Спасибо за интерес!'
    else:
        return 'To view results of analysis, visit ' + url + '. Thanks for your interest!'
