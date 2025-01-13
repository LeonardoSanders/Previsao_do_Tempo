from pprint import pprint
import requests

API_Key = "289c89fdae58929433efe0b4e59694c7"

class CityWeather():

    def __init__(self, name=''):
        self._name = name
        self.feels_like = 0
        self.humidity = 0
        self.temp_average = 0
        self.temp_max = 0
        self.temp_min = 0
        self.weather_cond = ''
    
    @property
    def city(self):
        return self._name
    
    @city.setter
    def city(self, value):
        self._name = value


    def do_request(self, query_city):
        q_city = query_city
        self._name = CityWeather.read_input('', q_city)

        base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+self._name
        weather_data = requests.get(base_url).json()

        return weather_data

    
    def check_status_city(self, code):
        if code['cod'] == '404':
            print(f'{code['message'].upper()}! Please, try another City!')
            return False
        else:
            return True
        
    
    def new_option_city(self):
        new_option = input("Please, enter your city: ").title().strip()
        return new_option

    
    def set_variables(self, weather_data):
        self.feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
        self.humidity = weather_data['main']['humidity']
        self.temp_average = round(weather_data['main']['temp'] - 273.15, 2)
        self.temp_max = round(weather_data['main']['temp_max'] - 273.15, 2)
        self.temp_min = round(weather_data['main']['temp_min'] - 273.15, 2)
        self.weather_cond = weather_data['weather'][0]['description']
        

    def read_input(self, city):
        city_name = city
        all_cities_file = open('all_cities_names.txt', 'r')
        all_cities = all_cities_file.read().splitlines()
        

        while True:
            find_city = all_cities.count(city_name)

            if find_city == 1 and city_name.isalpha():
                break
            else:
                print('Invalid city name, please try again!')
                city_name = input("Please, enter your city: ").title().strip()
        
        all_cities_file.close()

        return city_name
        

    def write_data_variables(self):
        with open('data.txt', 'w', encoding='utf8') as file:
            file.write(f'Average air temperature: {self.temp_average}°C\n')
            file.write(f'Maximum temperature: {str(self.temp_max)}°C\n')
            file.write(f'Minimum temperature: {str(self.temp_min)}°C\n')
            file.write(f'Feels Like: {str(self.feels_like)}°C\n')
            file.write(f'Relative Humidity: {str(self.humidity)}%\n')
            file.write(f'Weather condition: {str(self.weather_cond)}\n')

    def read_data_variables(self):
        with open('data.txt', 'r', encoding='utf-8') as file:
            print(file.read())

    
    def all_data_output(self, data_type, weather_data):
        while True:
            while 'N' != data_type != 'Y':
                data_type = input('Invalid value! Please, enter the correct value option [Y] or [N]: ').upper().strip()

            if data_type == 'Y':
                pprint(weather_data)
            
            print('\nThank you for using our services!')
            break