
# Змінні
x = "Hello world!"

# Текст (string)
text = "Hello world"
# Ціле число (integer)
x = 13
# Неціле число (float)
y = 1.4
# Логічне значення (bool)
value = True
value = False

# Списки
lst = [1, 5, 3, 7, 0, 3, 7, 14, 52]
lst[0] # 1;
lst[1] # 5
lst[7] # 14
# Довжина
len(lst) # 9

# До слів можна відноситись як до списків
string = "Hello world!"
string[0] # H
string[6] # w
len(string) # 12


# Умовні оператори if, else
variable = 0
if variable == 1:
    print("Одиниця")
else:
    print("Не одиниця")

# Оператори порівняння ==, !=, <, >, =<, =>
a = "Hello world"
a == "Hello world" # True/False

b = a == 'Hello world' # True


# TELEGRAM Бібліотека
# Імпортування необхідних функцій та класів з бібліотеки
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

# 
from dotenv import load_dotenv
import os

# Ім

# Задати змінну API_TOKEN, в якій зберігатиметься токен нашого бота
API_TOKEN = os.getenv("API_TOKEN")

def fetch_name():
    return "Maxim"





def privytannya(func):
    name = fetch_name()

    print(func(name))


def privit(name):
    return "Привіт, " + name + ", як справи?"

def goodbye(name):
    return "Прощавай, " + name




privytannya(privit)
privytannya(goodbye)
