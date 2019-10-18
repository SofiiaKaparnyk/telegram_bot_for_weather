import telebot
from Class_for_bot import Bot


TOKEN = '{YOUR TOKEN}'
bot = telebot.TeleBot(TOKEN)
weather_from_scrape = Bot().get_the_weather()
weather_from_api = Bot().get_the_weather_from_api()


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        weather_from_scrape
                    )


@bot.message_handler(commands=['help'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'This bot is created to send the weather.'
                    )


bot.polling(none_stop=True)