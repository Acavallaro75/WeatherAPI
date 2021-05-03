import requests
from tkinter import *
import math
from PIL import Image, ImageTk


# Function get_weather calls the weather API and returns JSON #
def get_weather(canvas):
    # City to get weather information about #
    city = search_bar.get()

    # API key used to access the API #
    api = 'c2de2bad67bf9dc6d39b5fdf4e98b15b'

    # API call to the URL below
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'

    # The response from the get request to the URL converted to JSON #
    json_data = requests.get(api_call).json()

    # Grabbing the individual temp value from the returned JSON #
    temperature = json_data['main']['temp']

    # Converting Kelvin to Fahrenheit #
    temperature = convert_to_fahrenheit(temperature)

    # Grabbing the individual feels_like value from the returned JSON #
    feels_like = json_data['main']['feels_like']

    # Converting Kelvin to Fahrenheit #
    feels_like = convert_to_fahrenheit(feels_like)

    # Grabbing the individual humidity value from the returned JSON #
    humidity = json_data['main']['humidity']

    # Grabbing the individual weather conditions from the JSON #
    conditions = json_data['weather'][0]['description']
    conditions = conditions.capitalize()

    # Grabbing the individual wind speed from the JSON #
    wind = json_data['wind']['speed']

    city_label.config(text=f'\n{city}')
    temp_label.config(text=f'{temperature} °F')
    weather_conditions.config(text=conditions)
    feels_like_label.config(text=f'\nFeels like: {feels_like} °F')
    humidity_label.config(text=f'Humidity: {humidity}%')
    wind_label.config(text=f'Wind Speed: {wind} MPH')


# convert_to_fahrenheit converts the passed value from Kelvin to Fahrenheit #
def convert_to_fahrenheit(temperature):
    return math.floor((temperature * 1.8) - 459.67)


# Main window #
root = Tk()

# Setting the size of the window #
root.geometry('480x480')

# Setting the title of the window #
root.title('Python Weather API')

# Logo #
logo = Image.open('images/weather_48px.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(root, image=logo)
logo_label.image = logo
logo_label.pack(side='top', anchor=NW)

# Search bar #
search_bar = Entry(root, width=50)
search_bar.pack(side='top', anchor=N)
search_bar.focus()
search_bar.bind('<Return>', get_weather)

# City name #
city_label = Label(root)
city_label.config(font=('poppins', 28))
city_label.pack(side='top', anchor=N)

# Temperature #
temp_label = Label(root)
temp_label.config(font=('poppins', 20))
temp_label.pack(side='top', anchor=N)

# Weather conditions #
weather_conditions = Label(root)
weather_conditions.config(font=('poppins', 14))
weather_conditions.pack(side='top', anchor=N)

# Feels like temperature #
feels_like_label = Label(root)
feels_like_label.config(font=('poppins', 14))
feels_like_label.pack(side='top', anchor=N)

# Humidity #
humidity_label = Label(root)
humidity_label.config(font=('poppins', 14))
humidity_label.pack(side='top', anchor=N)

# Wind conditions #
wind_label = Label(root)
wind_label.config(font=('poppins', 14))
wind_label.pack(side='top', anchor=N)

root.mainloop()
