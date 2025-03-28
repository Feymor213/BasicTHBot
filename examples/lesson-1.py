from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

async def start_command(update: Update, context):
    print("Message received: ", update.message.text)
    await update.message.reply_text("Bot started!")

app = Application.builder().token(API_TOKEN).build()
print("App built")

app.add_handler(CommandHandler("start", start_command))
app.run_polling(poll_interval=2)