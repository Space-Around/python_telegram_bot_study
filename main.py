import telebot
import uuid
import sqlite3

# генерируем название сохраняем файл в локалке с этим названием
# пишем в бд юсерайди или чатайди,  айди файла, синоним файла, расположение файла
# добавить возможность юзеру получать файл выбором из списка

bot = telebot.TeleBot("1783951936:AAHJvGb9F3gLwQLNT7dGveMbIK4I3W6HErE")

sent_videos = []
sent_pics = []
sent_gifs = []
sent_files = {'Videos': sent_videos, 'Pictures': sent_pics, 'Gifs': sent_gifs}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['list'])
def send_welcome(message):

    conn = sqlite3.connect(r"D:\DataBase\PTBS.db")
    cursor = conn.cursor()
    cursor.execute("select * FROM UsersData")
    results = cursor.fetchall()
    conn.close()

    print(results)

    files_names = []
    for i in results:
        files_names.append(i[2])

    bot.reply_to(message, f"Hey!\nYou have these files:\n{files_names}")

@bot.message_handler(commands=['search'])
def send_welcome(message):
    bot.reply_to(message, "Here the file you are looking for:")
    print(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo',''])
def photo(message):

    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    file_uuid = str(uuid.uuid4())
    chat_id = int(message.chat.id)
    file_name = f'image_{file_uuid}.jpg'

    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    file_path = (fr'D:\PycharmProjects\PTBS\{file_name}')

    conn = sqlite3.connect(r"D:\DataBase\PTBS.db")
    cursor = conn.cursor()
    conn.execute("INSERT INTO UsersData VALUES ( ?, ?, ?, ? ) ",
                 (chat_id, file_uuid, file_name, file_path))
    conn.commit()
    conn.close()

def create_db():
    conn = sqlite3.connect(r"D:\DataBase\PTBS.db")
    cursor = conn.cursor()
    conn.execute('''CREATE TABLE UsersData
                 (chat_id INTEGER ,file_uuid TEXT UNIQUE,
                 file_name TEXT NOT NULL,
                 fie_path TEXT NOT NULL);''')
    conn.commit()
    conn.close()

#create_db()

bot.polling()
