import os
from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

bot = telebot.TeleBot('5701552410:AAGwuJT70YtoLTqL0A1BgKWUFd1IuD0q4pQ')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)

keep_alive()
bot.polling(non_stop=True, interval=0)











