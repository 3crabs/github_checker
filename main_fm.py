import json
from flask import Flask, request
from answer import create_answer
from pymessenger.bot import Bot

with open('fm.json', 'r') as file:
    data = file.read()
obj = json.loads(data)
ACCESS_TOKEN = obj['ACCESS_TOKEN']
VERIFY_TOKEN = obj['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

app = Flask(__name__)


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args["hub.verify_token"]
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        bot.send_text_message(recipient_id, create_answer(message['message'].get('text'), 'eng'))
        return "Message Processed"


if __name__ == '__main__':
    app.run()
