import os
import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (filters,
                          MessageHandler,
                          ApplicationBuilder,
                          ContextTypes,
                          CommandHandler,
                          CallbackContext)
from budget_bot.firebase import add_expense

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN in your .env file.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="i'm a bot please talk to me")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_help = "add expenses using: /expense <amount> <category> [optional description]"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_help)


async def expense(update: Update, context: CallbackContext) -> int:
    """
    Handles the expense command
    """

    user_id = str(update.message.from_user.id)
    args = context.args

    if len(args) < 2:
        error_text = "Usage: /expense <amount> <category> [description]"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=error_text
            )
    try:
        amount = float(args[0])
    except ValueError:
        error_text = "Invalid amount! Please enter a valid number"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=error_text
            )
    category = args[1]
    description = " ".join(args[2:]) if len(args) > 2 else ""

    add_expense(user_id, amount, category, description, datetime.now)
    valid_text = f"Expense added!\n Amount: {amount}\n Category: {category}\n Description: {description or 'N/A'}"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=valid_text
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    expense_handler = CommandHandler('expense', expense)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(expense_handler)

    application.run_polling()
