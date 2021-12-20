import requests
import json
import telebot

bot = telebot.TeleBot('5088602776:AAH0RNUe186u7SMbdfmZLxtSOvSUbygQYnY')
api= requests.get('http://127.0.0.1:5000')
json_data = json.loads(api.content)

def rutasBGP():
    print(json_data)
rutasBGP()

@bot.message_handler(commands=['216.218.252.0'])
def greet(message):
    for object in json_data:
        dict = object
        reply = []
        for key in dict:
            data = key+" : "+dict[key]
            reply.append(data)
        reply = ' '.join(reply)
        bot.reply_to(message, reply)

bot.polling()