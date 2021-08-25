from django.shortcuts import render
from django.http import HttpResponse, request
import requests
import json

def home(request):
    user_inp = request.GET.get("zipcode")
    # print(type(user_inp), f"'{user_inp}'")
    zip = user_inp
    if zip is None or zip == "":
        zip = '60610'

    url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip}&distance=25&API_KEY="
    api_response = requests.get(url)
    # print(url)

    try:
        api = json.loads(api_response.content)
    except Exception as e:
        api = "There was an error with the request."
        return render(request, 'error.html', {})

    return render(request, 'home.html', {"api": api})

def about(request):
    return render(request, 'about.html', {})

def jumbotron(request):
    return render(request, 'jumbotron.html', {})
