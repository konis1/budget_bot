import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN in your .env file.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="i'm a bot please talk to me")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_help = "add expenses using: /expense <amount> <category> [optional description]"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_help)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()
