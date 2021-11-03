import telebot

bot = telebot.TeleBot("2023890748:AAFODf4AiK6HYlTR54iAu2rV5Tu_txnqMNA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello!!,\n how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text 
    bot.reply_to(message, message.text)

bot.infinity_polling()