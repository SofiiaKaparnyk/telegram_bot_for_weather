from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests


class Bot:

    def get_the_weather(self):
        website_url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D0%BE%D0%B2'
        with urlopen(website_url) as page:
            page_html = page.read()

        page_soup = soup(page_html, 'html.parser')

        find_all_span = page_soup.findAll('span')
        find_temp_today = page_soup.findAll('p', {'class': 'today-temp'})

        current_temp = find_temp_today[0].text
        minimum_temp = find_all_span[1].text
        maximum_temp = find_all_span[2].text

        weather = f'The minimum temperature today is {minimum_temp}. The maximum temperature is {maximum_temp}. ' \
                  f'Current temperature is {current_temp}. Enjoy the day!'
        return weather

    def get_the_weather_from_api(self):
        r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?q=Lviv&APPID={YOUR APPID}')
        current_temp = int(r.json()['main']['temp'] - 273.15)
        return f'Current temperature in Lviv is {current_temp}°.'


