from pprint import pprint

class CityWeather():

    def __init__(self, city):
        self._city = city
        self.feels_like = 0
        self.humidity = 0
        self.temp_average = 0
        self.temp_max = 0
        self.temp_min = 0
        self.weather_cond = ''
    
    @property
    def city(self):
        return self._city

    
    def set_variables(self, weather_data):
        self.feels_like = round(weather_data['main']['feels_like'] - 273.15, 2)
        self.humidity = weather_data['main']['humidity']
        self.temp_average = round(weather_data['main']['temp'] - 273.15, 2)
        self.temp_max = round(weather_data['main']['temp_max'] - 273.15, 2)
        self.temp_min = round(weather_data['main']['temp_min'] - 273.15, 2)
        self.weather_cond = weather_data['weather'][0]['description']
        

    def read_input(self):
        city_name = self._city
        
        while True:
            if not city_name.isnumeric():
                try:
                    result = str(city_name)
                    break
                except:
                    print('Invalid city name, please try again!')
                    city_name = input("Please, enter your city: ").lower().strip()
            else:
                print('Invalid city name, please try again!')
                city_name = input("Please, enter your city: ").lower().strip()

        return result
    

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