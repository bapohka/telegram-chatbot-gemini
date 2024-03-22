# pip install pyTelegramBotAPI google-generativeai -U
import telebot

import google.generativeai as genai


# Токен вашого бота, який ви отримали від BotFather
TELEGRAM_API_TOKEN = 'YOUR_TG_BOT_KEY'

# place GEMINI API key
GEMINI_API_KEY = "YOUR_GEMINI_KEY"
genai.configure(api_key=GEMINI_API_KEY)

# Set up the gemini model
generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# https://ai.google.dev/docs/safety_setting_gemini 
# BLOCK_NONE  / BLOCK_ONLY_HIGH  / BLOCK_MEDIUM_AND_ABOVE / BLOCK_LOW_AND_ABOVE 
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
# можна використовувати модель за замовчуванням, чи будь-яку іншу gemini-1.0-pro-latest // or gemini-pro
model = genai.GenerativeModel(model_name='gemini-1.0-pro-latest', 
                              generation_config=generation_config, # type: ignore
                              safety_settings=safety_settings)

# Створюємо екземпляр боту
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


chat = model.start_chat(history=[])

# задаємо команди для телеграм боту
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я телеграм-бот, який працює з нейромоделю Gemini pro. Створений юзером @bapohka. Я маю знижений рівень цензури. Запитай в мене будь-що")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    question = chat.send_message(message.text)
    try:
        response = question.text 
        bot.reply_to(message,response)
    except ValueError:
        # If the response doesn't contain text, check if the prompt was blocked.
        bot.reply_to(message,response.prompt_feedback) # type: ignore
        # Also check the finish reason to see if the response was blocked.
        bot.reply_to(message,response.candidates[0].finish_reason) # type: ignore
        # If the finish reason was SAFETY, the safety ratings have more details.
        bot.reply_to(message,response.candidates[0].safety_ratings) # type: ignore

# Запуск бота
bot.infinity_polling(timeout=10, long_polling_timeout=5)

