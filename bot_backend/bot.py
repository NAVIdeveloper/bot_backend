from telebot import *
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_backend.settings')

django.setup()

from WebApp.models import *

TOKEN = "6012621974:AAHxPgEgqhdgfMQfvHvPJmEWQTDDgAiJLQI"
host = "https://127.0.0.1:8000/"
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def Command_start(message):
	markup = types.ReplyKeyboardMarkup()
	for i in CodeFile.objects.filter(user=message.from_user.id):
		markup.add(types.KeyboardButton(i.file_name))
	
	bot.send_message(message.from_user.id,"Welcome",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Command_text(message):
	if len(list(CodeFile.objects.filter(user=message.from_user.id,file_name=message.text))) != 0:
		code = CodeFile.objects.get(user=message.from_user.id,file_name=message.text)
		markup  = types.InlineKeyboardMarkup()
		markup.add(
			types.InlineKeyboardButton("view",web_app=types.WebAppInfo(f"{host}/code/{code.id}/?user={message.from_user.id}"))
		)
		bot.send_message(message.from_user.id,f"view code > {message.text}",reply_markup=markup)

@bot.message_handler(content_types=['document'])
def Command_new(message):
	fid=message.document.file_id
	inf=bot.get_file(fid)
	f=bot.download_file(inf.file_path)
	CodeFile.objects.create(user=message.from_user.id,
		file_name=message.document.file_name,
		code=f.decode(),
		lang=Lexer.objects.last(),
		style=Style.objects.last(),
	)
	Command_start(message)		
	
bot.polling()
