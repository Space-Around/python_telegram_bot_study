import telebot

bot = telebot.TeleBot("1783951936:AAHJvGb9F3gLwQLNT7dGveMbIK4I3W6HErE")

sent_videos = []
sent_pics = []
sent_gifs = []

sent_files = {'Videos': sent_videos, 'Pictures': sent_pics, 'Gifs': sent_gifs}

@bot.message_handler(content_types=['photo'])
def photo(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    #генерируем название сохраняем файл в локалке с этим названием
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    print(message)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['list'])
def send_welcome(message):
    bot.reply_to(message, "You have access to these files:")


@bot.message_handler(commands=['search'])
def send_welcome(message):
    bot.reply_to(message, "Here the file you are looking for:")
    print(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
