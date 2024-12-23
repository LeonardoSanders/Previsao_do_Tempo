import requests
from pprint import pprint

API_Key = "289c89fdae58929433efe0b4e59694c7"

city = input("Informe sua cidade: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)