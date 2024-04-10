# import requests
# import datetime as dt

# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
# API_KEY = open('api_key.txt', 'r').read()

# CITY = "New York"

# url = f'{BASE_URL}q={CITY}&appid={API_KEY}'
# response = requests.get(url).json()


# sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
# sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
# country_name = response['sys']['country']


# print(f'{CITY} is a city in {country_name}')
# print(f'sunrise time in {CITY} is {sunrise_time}')
# print(f'sunset time in {CITY} is {sunset_time}')
