# Імпортування необхідних функцій та класів з бібліотеки
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
from dotenv import load_dotenv
import os

# Завантаження даних з .env
load_dotenv()

# Задати змінну API_TOKEN, в якій зберігатиметься токен нашого бота (взяли від BotFather)
API_TOKEN = os.getenv("API_TOKEN")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello world!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help text.")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")

# Перевіряємо правильність завантаження токену
print("token", API_TOKEN)

# Підключаємось до телеграму за допомогою токена
app = Application.builder().token(API_TOKEN).build()
print("App built.")

# Додаємо команди
app.add_handler(CommandHandler("start", start_command)) # /start
app.add_handler(CommandHandler("help", help_command)) # /help
app.add_handler(CommandHandler("custom", custom_command)) # /custom

# Запускаємо нашу програму
print("Running polling")
app.run_polling(poll_interval=2)