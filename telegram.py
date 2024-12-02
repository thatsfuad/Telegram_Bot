import telebot


token = "7839705314:AAFDb9Se6D-UkJYt1oRWZ0VI2P1u8v-7eRA"

bot = telebot.TeleBot(token)

@bot.message_handler(['start']) # jodi ami cai start er sathe aro kono command dile ai fuction a colbe taile list akare dite pari
def start(message):
    bot.reply_to(message,"Welcome to fuad world")


@bot.message_handler(['help']) 
def help(message):
    bot.reply_to(message,"""
    /start -> Greeting
    /help -> If you want use my bot for calculate any number ..
                 
    """)

@bot.message_handler() 
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e :
        msg = "This can't be evaluated " 
    bot.reply_to(message,msg)

bot.polling()