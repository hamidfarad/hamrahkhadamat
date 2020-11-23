from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler,Filters
import os
PORT = int(os.environ.get('PORT', 5000))

class Mybot ():
    def __init__(self):
        pass

    def start (self , update , context):
        context.bot.send_message(chat_id=update.message.chat.id, text="I")
        print(update.message.chat.id)
        context.bot.send_message(chat_id=update.message.chat.id , text=  "@"+update.message.from_user.username + " _ " + update.message.text)

    def text(self , update , context):
        context.bot.send_message(chat_id=update.message.chat.id , text=  "@"+update.message.from_user.username + " _ " + update.message.text)
        user = update.message.from_user
        print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
        print(update.message.chat.first_name)
        context.bot.forwardMessage(chat_id = 156298391 , from_chat_id=update.message.chat.id  , message_id =update.message.message_id , disable_notification = False)

    def offf (self , update , context):
        textoff = update.message.text 
        if textoff == "off":
            pass
        
    def main(self):
        updater = Updater("1414294529:AAF-Hjd9HuYnsotb4nfUFr9JkIy8K8IDEFI")
    
        updater.dispatcher.add_handler(CommandHandler('start' , self.start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text , self.text , pass_user_data=True))
        updater.dispatcher.add_handler(MessageHandler(Filters.text , self.offf ))

        
        TOKEN = "1414294529:AAF-Hjd9HuYnsotb4nfUFr9JkIy8K8IDEFI"
        updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
        updater.bot.setWebhook('https://hamrahkhadamat.herokuapp.com/' + TOKEN)
        updater.idle()

bot = Mybot ()
bot.main()
