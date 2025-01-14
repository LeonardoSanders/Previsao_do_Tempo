from city_weather import CityWeather

city = CityWeather()

print('Welcome to Real Time Weather Information Program')
query_city = input("Please, enter your city: ").title().strip()
weather_data = city.do_request(query_city)


while True:
    city_status = city.check_status_city(weather_data)
    if not city_status:
        city._name = city.new_option_city()
        city._name = city.read_input(city._name)
        weather_data = city.do_request(city._name)
    else:
        break

def main():
    city.set_variables(weather_data)
    city.write_data_variables()
    city.read_data_variables()

    data_type = input('\nDo you want all data information? [Y/N]: ').upper().strip()
    city.all_data_output(data_type, weather_data)


if __name__ == '__main__':
    main()
