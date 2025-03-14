from typing import Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application
import os, random

load_dotenv()

API_TOKEN: Final = os.getenv("API_TOKEN")
BOT_USERNAME: Final = "@test_hubnusle_bot"

def save_user(user: str):
  try:
    with open("./users.txt", 'a') as file:
      file.write('\n'+user)
  except FileNotFoundError:
    open("./users.txt", 'x')
    save_user()


def get_users():
  try:
    with open("./users.txt", 'r') as file:
      content = file.read()
      users = content.split('\n')
      users = list(filter(lambda user: bool(user), users))
      return users
  except FileNotFoundError:
    open("./users.txt", 'x')
    get_users()

def drop_users():
  try:
    with open("./users.txt", 'w') as file:
      file.write('')
  except FileNotFoundError:
    open("./users.txt", 'x')
    drop_users()

async def select_best_user_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

  if update.message.chat.type != "group":
    await update.message.reply_text("Not in a group!")
    return

  users = get_users()
  selected_user = random.choice(users)
  await update.message.reply_text(f"User {selected_user} is gay.")

async def register_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

  if update.message.chat.type != "group":
    await update.message.reply_text("Not in a group!")
    return

  user = update._effective_user.name
  if user in get_users():
    await update.message.reply_text(f"User {user} already registered!")
    return
  
  save_user(user)
  await update.message.reply_text(f"User {user} successfully registered!")

async def print_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
  users = get_users()
  if users:
    await update.message.reply_text(users)
    return
  
  await update.message.reply_text("No users registered")

if __name__ == "__main__":
  load_dotenv()
  print("token", API_TOKEN)
  print("name", BOT_USERNAME)

  app = Application.builder().token(API_TOKEN).build()
  print("App built.")

  app.add_handler(CommandHandler("select", select_best_user_command))
  app.add_handler(CommandHandler("register", register_user))
  app.add_handler(CommandHandler("getusers", print_users))

  print("Running polling")
  app.run_polling(poll_interval=2)