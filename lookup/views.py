from django.shortcuts import render
import requests
import json
from . import secrets

def air_quality(request):
    user_inp = request.GET.get("zipcode")
    # print(type(user_inp), f"'{user_inp}'")
    zip = user_inp
    if zip is None or zip == "":
        zip = '60610'

    # the key is in the database
    API_KEY = secrets.airquality_key
    url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip}&distance=25&API_KEY={API_KEY}"
    api_response = requests.get(url)
    # print(url)

    try:
        api = json.loads(api_response.content)
    except Exception as e:
        api = "There was an error with the request."
        return render(request, 'error.html', {})

    return render(request, 'home.html', {"api": api})


def fetch_weather(q=None, id=None, zip=None):
    url1 = f'http://api.openweathermap.org/data/2.5/weather?'
    api_key = secrets.weather_key
    url3 = f'appid={api_key}&units=imperial'

    url2 = 'q=Chicago&'
    if id:
        url2 = f'id={id}&'
    elif zip:
        url2 = f'zip={zip}&'
    else:
        url2 = f'q={q}&'
    url2 = url2.replace("'", "")
    url2 = url2.replace('"', "")

    api_url = url1 + url2 + url3
    r = requests.get(api_url).json()
    return r


def isdigits(x):
    digitsFound = False
    for r in x:
        if not (r in '0123456789'):
            return False
        digitsFound = True
    return digitsFound

def weather(request):
    args = request.GET.get('args','').strip()
    user_inp = request.GET.get("zipcode", '')

    q = None
    zip = None

    if isdigits(args):
        zip = args
    else:
        q = args

    if isdigits(user_inp):
        zip = user_inp

    if zip is None and q == '':
        q = 'Chicago'

    weather = fetch_weather(q=q, zip=zip)

    if weather['cod'] == '404':
        weather['coord'] = {'lon': -87.65, 'lat': 41.85}

    return render(request, 'weather.html', {'weather': weather})



def about(request):
    return render(request, 'about.html', {})

def jumbotron(request):
    return render(request, 'jumbotron.html', {})
