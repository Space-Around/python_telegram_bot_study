import telebot

bot = telebot.TeleBot("1783951936:AAHJvGb9F3gLwQLNT7dGveMbIK4I3W6HErE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['list'])
def send_welcome(message):
	bot.reply_to(message, "You have access to these files:")

@bot.message_handler(commands=['search'])
def send_welcome(message):
	bot.reply_to(message, "Here the file you are looking for:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()