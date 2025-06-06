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
    chat_type = update.message.chat.type # Група чи особистий чат
    text = update.message.text # Витягуємо текст, який написав користувач

    print(f"User ({update.message.chat.id}) in {chat_type}: \"{text}\" ")
    
    response = handle_response(text)

    print(f"Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


# Перевіряємо правильність завантаження токену
print("token", API_TOKEN)

# Підключаємось до телеграму за допомогою токена
app = Application.builder().token(API_TOKEN).build()
print("App built.")

# Додаємо команди
app.add_handler(CommandHandler("start", start_command)) # /start
app.add_handler(CommandHandler("help", help_command)) # /help
app.add_handler(CommandHandler("custom", custom_command)) # /custom

app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.add_error_handler(error)

print("Running polling")
app.run_polling(poll_interval=2)