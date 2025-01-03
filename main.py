import requests
from pprint import pprint

API_Key = "289c89fdae58929433efe0b4e59694c7"

print('Welcome to the Weather Information Program')
city = input("Please, enter your city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
humidity = weather_data['main']['humidity']
temp_average = round(weather_data['main']['temp'] - 273.15, 2)
temp_max = round(weather_data['main']['temp_max'] - 273.15, 2)
temp_min = round(weather_data['main']['temp_min'] - 273.15, 2)
weather_cond = weather_data['weather'][0]['description']

print(f'\nAverage air temperature: {temp_average}°C')
print(f'Maximum temperature: {temp_max}°C')
print(f'Minimum temperature: {temp_min}°C')
print(f'Feels Like: {feels_like}°C')
print(f'Relative Humidity: {humidity}%')
print(f'Weather condition: {weather_cond}')

data_type = input('\nDo you want all data information? [Y/N]: ').upper().strip()

while True:
    while 'N' != data_type != 'Y':
        data_type = input('Invalid value! Please, enter the correct value option [Y] or [ N]: ').upper().strip()

    if data_type == 'Y':
        pprint(weather_data)
    
    print('Thank you for using our services!')
    break