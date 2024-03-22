# telegram-chatbot-gemini
Telegram bot, using gemini-api for answers

## **PREREQUIREMENTS**
Треба мати встановленими python(зі встановленими PATH), visual studio(чи що вам комфортніше)

- Створити бота через https://t.me/BotFather
- Скопіювати api-key вашого бота до TELEGRAM_API_TOKEN = 'YOUR_TG_BOT_KEY'

- Створити api-key для роботи з Gemini https://ai.google.dev/ чи одразу https://makersuite.google.com/app/apikey
- Скопіювати api-key до GEMINI_API_KEY = "YOUR_GEMINI_KEY"
Ця сторінка недоступна з України та Європи, то ж вам необхідно включити впн у локаціях: Америка, Туреччина, Грузія, чи якусь азіатську країну - Таїланд, Тайвань, Сінгапур, Малайзія. Далі, Для використання Gemini, щоб бот працював, впн повинен бути включеним при використанні.

## **Installation**
- Встановити бібліотеки:
'''bash
pip install pyTelegramBotAPI google-generativeai -U
'''

Запустити у терміналі, та користуватися ботом. 
'''bash
python main.py
'''
Бот запущений локально, то ж поки ваш комп'ютер буде запущений - ваш бот буде працювати.

Змінити рівень цензури бота можна у safety_settings, за замовчуванням в бота нема жодної цензури.
Якщо відповіді не було, можливо був таймаут на опрацювання запиту, то ж просто спитайте бота те саме ще раз

