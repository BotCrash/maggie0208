import telebot


bot = telebot.TeleBot("1910033477:AAFgTbZ6E-_KcgjEoQNpoPDSegx_ZGjy3Pk", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(commands=['uwu'])
def send_welcome(message):
	markup = types.ForceReply(selective=False)
bot.send_message(chat_id, "Send me another word:", reply_markup=markup)

	
"""# ForceReply: forces a user to reply to a message
# Takes an optional selective argument (True/False, default False)
markup = types.ForceReply(selective=False)
tb.send_message(chat_id, "Send me another word:", reply_markup=markup)
"""
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
	



bot.polling()

