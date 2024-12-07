import telebot

token = "7839705314:AAFDb9Se6D-UkJYt1oRWZ0VI2P1u8v-7eRA"

bot = telebot.TeleBot(token)

@bot.message_handler(['start']) # jodi ami cai start er sathe aro kono command dile ai fuction a colbe taile list akare dite pari
def start(message):
    bot.reply_to(message,"Hello,Welcome to fuad world")
    bot.reply_to(message,"/help")



@bot.message_handler(['help']) 
def help(message):
    bot.reply_to(message,"""
    /start -> Welcome message
    /Calculator -> If you want use my bot for calculate any number ..
    /content -> About me more 
                 
    """)

@bot.message_handler(['content']) 
def content(message):
    bot.reply_to(message,"""
    /facebook ->To view my Facebook id
    /Fiverr -> To view my Fiverr gig
    /Linkdin -> To view my Linkdin id
    /Portfolio -> To view my Portfolio
    /Github -> To view my Github account
    /Contact_Number -> To view my Contact Number
    /For my gmail -> To view my Gmail
                 
    """)

@bot.message_handler(['Calculator']) 
def Calculator(message):
    bot.reply_to(message,"Yes,Sure! You use my bot for calculate any number")

@bot.message_handler(['facebook']) 
def facebook(message):
    bot.reply_to(message,"https://www.facebook.com/profile.php?id=100070616027561")
 
@bot.message_handler(['Fiverr']) 
def Fiverr(message):
    bot.reply_to(message,"https://www.fiverr.com/s/BRX7rq7")

@bot.message_handler(['Linkdin']) 
def Linkdin(message):
    bot.reply_to(message,"https://www.linkedin.com/in/fuad-hasan-rabby04/")

@bot.message_handler(['Portfolio']) 
def Portfolio(message):
    bot.reply_to(message,"https://thatsfuad.github.io/")

@bot.message_handler(['Github']) 
def Github(message):
    bot.reply_to(message,"https://github.com/thatsfuad")

@bot.message_handler(['Contact_Number']) 
def Contact_Number(message):
    bot.reply_to(message,"01568380004")

@bot.message_handler(['For my gmail']) 
def For_my_gmail(message):
    bot.reply_to(message,"Yes,Sure! You use my bot for calculate any number")

@bot.message_handler() 
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e :
        msg = "This can't be evaluated " 
    bot.reply_to(message,msg)

bot.polling()