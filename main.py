import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv  # pip install python-dotenv

# .env faylni yuklash
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")  # tokenni o'qish

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Men ishlayapman 🚀")

def main():
    updater = Updater(token=API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    print("Bot ishga tushdi...")
    updater.idle()

if __name__ == "__main__":
    main()
