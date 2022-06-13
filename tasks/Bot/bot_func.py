import requests
import json
from datetime import datetime

def get_token():
    with open('token.txt', 'r') as token_file:
        return str(token_file.readlines()[0].strip())

def get_weather_token():
    with open('token.txt', 'r') as token_file:
        return str(token_file.readlines()[1].strip())

def get_location_data(token, lat, lon):
    get_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token}&q={lat}%2C{lon}&language=ru-ru&details=false&toplevel=false'
    loc_key = json.loads(requests.get(get_key).text)['Key']
    loc_country = json.loads(requests.get(get_key).text)['Country']['LocalizedName']
    loc_city_area = json.loads(requests.get(get_key).text)['AdministrativeArea']['LocalizedName']
    loc_city = json.loads(requests.get(get_key).text)['LocalizedName']
    return [loc_key, loc_country, loc_city, loc_city_area]

def get_forecast(token, loc_key):
    get_weather = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{loc_key}?apikey={token}&language=ru-ru&details=true&metric=true'
    five_d_forecast = json.loads(requests.get(get_weather).text)['DailyForecasts']
    forecast = ''
    for day in five_d_forecast:
        date = datetime.strptime(day['Date'], '%Y-%m-%dT%H:%M:%S%z').date()
        sunrise = datetime.strptime(day['Sun']['Rise'], '%Y-%m-%dT%H:%M:%S%z').time()
        sunset = datetime.strptime(day['Sun']['Set'], '%Y-%m-%dT%H:%M:%S%z').time()
        min_t = day['Temperature']['Minimum']['Value']
        max_t = day['Temperature']['Maximum']['Value']
        day_weather = day['Day']['IconPhrase']
        night_weather = day['Night']['IconPhrase']
        output = f'Дата: {date}\n' \
                 f'Максимальная температура: {max_t} \u00b0C\n' \
                 f'Минимальная температура: {min_t} \u00b0C\n' \
                 f'Погода днем: {day_weather}\n' \
                 f'Погода ночью: {night_weather}\n' \
                 f'Восход: {sunrise}\n' \
                 f'Закат: {sunset}\n\n'
        forecast += output
    return forecast