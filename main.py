import os
import telebot

API_TOKEN = os.getenv("BOT_TOKEN", "8320831037:AAFFnk9eatszVHGQZCYRSn3IYFMxYtWb8fw")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I’m your business assistant bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
