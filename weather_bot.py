import telebot
from telebot import types
import requests
import json

# 8375354134:AAF2Tro9Lv1SsxwzddbjYG4BaJcjvD4YDgA

weather_bot = telebot.TeleBot('8375354134:AAF2Tro9Lv1SsxwzddbjYG4BaJcjvD4YDgA')

@weather_bot.message_handler(commands=['start'])
def greet(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('Weather')
    weather_bot.send_message(message.chat.id, 'Welcome to chat with me! How can I help you?', reply_markup=keyboard)


@weather_bot.message_handler(func=lambda message: message.text == 'Weather')
def weather(message):
    weather_bot.send_message(message.chat.id, 'Please, write me a city weather you would like to know')

@weather_bot.message_handler()
def get_weather_info(message):
    correct_message = message.text.title()

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={correct_message}&appid=e90fab7014064d2c88795d9fd95afa6f").text
        weather_info = json.loads(response)
        print(weather_info)
        weather = f'Weather in {correct_message} is {weather_info['weather'][0]['description']}.'
        temperature = f'Temperature: {round(weather_info['main']['temp'] - 273.15, 1)} °C'
        feel_temp = f'Feels like: {round(weather_info['main']['feels_like'] - 273.15, 1)} °C'
        pressure = f'Pressure of atmosphere: {round(weather_info['main']['pressure'] * 0.75, 1)} mm Hg'
        humidity = f'Humidity: {weather_info['main']['humidity']} %'
        wind_speed = f'Wind speed: {weather_info['wind']['speed']} m/s'

        general_info = '\n'.join((weather, temperature, feel_temp, pressure, humidity, wind_speed))


        weather_bot.send_message(message.chat.id, general_info)
    except Exception:
        weather_bot.send_message(message.chat.id, 'Sorry, but I can\' find this city or incorrect city name. Please, check the correcting written of city name.')

weather_bot.infinity_polling()