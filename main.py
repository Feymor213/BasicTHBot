from typing import Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
import os

load_dotenv()

API_TOKEN: Final = os.getenv("API_TOKEN")
BOT_USERNAME: Final = "@test_hubnusle_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello world!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help text.")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")

def handle_response(text: str) -> str:
    text = text.lower()

    responses: dict = {
        'hello': "Hi there",
        'how are you': "I'm good"
    }

    if text in responses:
        return responses[text]
    
    return "I do not understand"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: \"{text}\" ")

    if message_type != "group":
        response: str = handle_response(text)

    print(f"Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    load_dotenv()
    print("token", API_TOKEN)
    print("name", BOT_USERNAME)

    app = Application.builder().token(API_TOKEN).build()
    print("App built.")

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Running polling")
    app.run_polling(poll_interval=2)