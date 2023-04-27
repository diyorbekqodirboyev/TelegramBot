import telebot as tb

bot = tb.TeleBot("Your token")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message, 'Hello, welcome to my bot.')
	
bot.polling()