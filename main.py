import requests
from city_weather import CityWeather


API_Key = "289c89fdae58929433efe0b4e59694c7"

print('Welcome to the Weather Information Program')

query_city = input("Please, enter your city: ").lower().strip()

city = CityWeather(query_city)

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city.city

weather_data = requests.get(base_url).json()



def main():
    city.read_input()
    city.set_variables(weather_data)
    city.write_data_variables()
    city.read_data_variables()

    data_type = input('\nDo you want all data information? [Y/N]: ').upper().strip()
    city.all_data_output(data_type, weather_data)


if __name__ == '__main__':
    main()
