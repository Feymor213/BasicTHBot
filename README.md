# Initial setup guide

### Бібліотеки для проекту
- **python-telegram-bot** - основна бібліотека (обов'язкова для запуску бота):
- *(за бажанням для покращення безпеки)* **python-dotenv** - допоміжна бібліотека для отримання чутливих даних з окремого файлу (.env)
- *(лише для бота AIbot.py) **openai** - бібліотека для комунікації з OpenAI API (ChatGPT та ін.).

Всі бібліотеки перечислені у файлі **requirements.txt** для автоматичного встановлення за допомогою pip
Встановити всі бібліотеки з файлу **requirements.txt**: pip install -r requirements.txt

## Git


### Env variables
- API_TOKEN - access token acquired from telegram BotFather.
- BOT_USERNAME - your bot's username.
- OPENAI_TOKEN (Only when running AIBot) - token for openai API to generate response with LLM
