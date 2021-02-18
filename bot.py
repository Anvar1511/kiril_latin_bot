import	telebot
import config
# from rassilka import *
from transliterate import to_cyrillic, to_latin

joinedFile = open("/home/Anvarjon1511/joined.txt", "r")
joinedUsers = set()


bot = telebot.TeleBot(config.TOKEN)



for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
	if not str(message.chat.id) in joinedUsers:
		joinedFile = open("/home/Anvarjon1511/joined.txt", "a")
		joinedFile.write( str(message.chat.id)+"\n")
		joinedUsers.add(message.chat.id)
	bot.send_message(message.chat.id, "Assalomu aleykum, {0.first_name}! \nMen - <b>{1.first_name}</b>, matnlarni lotindan kirillga va kirilldan lotinga o`zgartiraman. <b>Matnlarni menga yuboring!</b>".format(message.from_user, bot.get_me()),
	    parse_mode='html')

@bot.message_handler(commands=['bot_info'])
def info(message):
    numb_subs = len(joinedUsers)
    bot.send_message(message.chat.id, "Mazkur bot foydalanuvchilari soni: {0} ta.".format(numb_subs))


@bot.message_handler(commands=['reklamayuborvor'])
def mess(message):
	for user in joinedUsers:
	    photo = open('/home/Anvarjon1511/rasm_nomi', 'rb')
	    bot.send_photo(user, photo, """""", parse_mode='html')

# @bot.message_handler(commands=['start'])
# def welcome(message):
# 	bot.send_message(message.chat.id, "Assalomu aleykum, {0.first_name}! \nMen - <b>{1.first_name}</b>, matnlarni lotindan kirillga va kirilldan lotinga bexato o`zgartiraman. <b>Matnlarni menga yuboring!</b>".format(message.from_user, bot.get_me()),
# 		parse_mode='html')
#============================================================================ transilator start =============================================

#=============================================================================transilator end================================================
@bot.message_handler(content_types=['text'])
def translate(message):
    input_text = message.text
    if input_text.isascii():
        room = to_cyrillic(input_text)
    else:
        room = to_latin(input_text)

    bot.send_message(message.chat.id, room)


#run
bot.polling(none_stop=True)

