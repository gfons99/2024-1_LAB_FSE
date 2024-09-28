import telebot

bot = telebot.TeleBot("7278491826:AAErSRgcXVHu3LE-JfIwqvwXuAY9XBnFjE8")

@bot.message_handler(commands=['start'])
def send_start(message):
	bot.reply_to(message, "Mensaje de bienvenida.")
	
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Mensaje de ayuda.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
