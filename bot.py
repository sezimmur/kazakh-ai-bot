import openai
import telebot
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Сәлем! Мен қазақ тілінде сөйлейтін Telegram ботпын!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_input = message.text
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Сен ақылды Telegram ботсың. Сен тек қазақ тілінде сөйлейсің."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, "Қате шықты: " + str(e))

bot.polling()
