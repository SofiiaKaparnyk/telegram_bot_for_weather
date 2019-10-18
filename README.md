# TelegramBot_for_weather

This bot allows you to receive the weather in Lviv when you click '/start' in the telegram.

File Bot.py allows you to run the bot. In the line "TOKEN = 'Your token'" you need to input your token.
Go to the BotFather (if you open it in desktop, make sure you have the Telegram app), then create a new bot by sending the /newbot command.
Follow the steps until you get the username and token for your bot. 

Also, the file - untests.py checks whether the Class_for_bot works correctly and returns the weather.

You may receive the weather from Sinoptik - get_the_weather function, or from OpenWeatherMap - https://openweathermap.org for Lviv - get_the_weather_from api function.

"r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Lviv&APPID={your APPID}')" - APPID will be available, after you log in on the website of OpenWeatherMap.


