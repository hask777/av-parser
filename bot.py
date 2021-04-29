import telebot

bot = telebot.TeleBot("1799280940:AAG7DKicYzMLX7zzXYJg5ZcrHOPTrqdkrdw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling() 