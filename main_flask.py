'''
Simple telegram bot.
For local launch activate first
venv_path => D:\PY\py_venv\telebot_flask_venv\Scripts\Activate.ps1

environment variables must be set:
API_TOKEN - both local and prod
HEROKU - just in prod (to define where we launch the bot)
'''

import logging
import random
import os

from flask import Flask, request

import telebot

from phrases import PHRASES
from parameters import *

# initialliza the bot
bot = telebot.TeleBot(API_TOKEN)

# to get info in console
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# hanlde bot commands and text listener


@bot.message_handler(commands=['start', 'help'])
def handler_start(message):
    reply = "Hello, I will reply to your messages with phrases inspired by Leonid The Manager.\n\
You can also recieve the random one from me with the /speak command."

    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['speak'])
def handler_speak(message):
    '''
    The speak command will be replied by random phrase.
    '''
    reply = random.choice(PHRASES)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(content_types=['text'])
def handler_text(message):
    '''
    Each message in the chat will be checked, and send to reply generator function.
    '''
    text = message.text.split()
    print(text)
    reply = reply_generator(text)
    if reply:
        bot.send_message(message.chat.id, reply)


def reply_generator(text):
    '''
    If the text contains the words which are present in PHRASES 
    (and the word is larger than 2 letters), then the one if these phrases will be selected randomly.
    '''
    fit_phrases = []
    for word in text:
        for ph in PHRASES:
            if word.lower() in ph.lower() and len(word) > 2:
                print(word, ph)
                fit_phrases.append(ph)
    if fit_phrases:
        return random.choice(fit_phrases)


def main(bot):
    '''
    The function checks if bot runs local or on heroku
    so we need to add HEROKU var to PATH variables on heroku app.
    If we are on heroku app, run simple flask server.

    Or if we're on local machine just start polling the bot.
    In this case remove webhook, because it will throw an error if the one left from previous launch.
    '''

    if "HEROKU" in list(os.environ.keys()):
        server = Flask(__name__)

        @server.route("/", methods=['POST'])
        def getMessage():
            bot.process_new_updates(
                [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "I'm looking for answer.", 200

        @server.route("/")
        def webhook():
            bot.remove_webhook()
            bot.set_webhook(url=WEBHOOK_HOST)
            return "I'm alive and waiting for your messages", 200

        server.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)

    else:
        bot.remove_webhook()
        bot.polling(none_stop=True)


if __name__ == '__main__':
    main(bot)
