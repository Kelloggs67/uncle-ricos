from django.shortcuts import render
from django.http import HttpResponse
import requests
from ipstack import GeoLookup
from datetime import datetime
from .models import *
# Create your views here.

def main():

    #GET LOCATION
    geo_lookup = GeoLookup("3f6e3ea0f53c0a3eeb2ebd578f3d74f3")
    location = geo_lookup.get_own_location()
    lon = location['longitude']
    lat = location['latitude']
    city = location['city']

    print(city)

    #GET CURRENT WEATHER
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid=7acfccf49d5888267f2a1348496ac9a2'
    weather_response = requests.get(url.format(lat, lon)).json()

    #GET MARINE INFO
    marine_url = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=7b48a0b9095643daa99232159211102&q={}, {}&format=json&tp=1'
    marine_response = requests.get(marine_url.format(lat, lon)).json()

    #GET CURRENT TIME
    now = datetime.now()
    current_time = int(now.strftime("%H"))
    current_minute = int(now.strftime("%M"))
    print("Current Time =", current_time, current_minute)

    if current_minute >= 45 and current_time != 23:
        current_time += 1

    print(current_time)

    #GET SUNRISE AND SUNSET INFO
    sunset_full_time = marine_response['data']['weather'][0]['astronomy'][0]['sunset']
    sunrise_full_time = marine_response['data']['weather'][0]['astronomy'][0]['sunrise']
    sunrise_code = int(sunrise_full_time[:2])
    sunset_code = int(sunset_full_time[:2])

    if sunset_full_time[-2:] == 'PM':
        sunset_code += 12

    if sunrise_full_time[-2:] == 'PM':
        sunrise_code += 12

    if current_time < sunset_code and current_time > sunrise_code:
        day = 'day'
    else:
        day = 'night'

    print(sunset_code, sunrise_code)


    #GET SPECIFIC DATA
    forecast = marine_response['data']['weather'][0]['hourly'][current_time]
    temp_f = str(round(weather_response['main']['temp']))
    water_temp_f = forecast['waterTemp_F']
    icon = 'images/world-weather-online-set/PNGs_128x128/'+ day + '/' + forecast['weatherCode']


    #CONTEXT
    marine_weather = {
        "temp": temp_f + '°F',
        "water": water_temp_f + '°F',
        "icon": icon,
    }

    context = ('marine_weather', marine_weather)


    return context

def scroll(request):

    nav = main()
    products = Product.objects.all()
    context = {nav[0]: nav[1], 'products': products}

    return render(request, 'store/scroll.html', context)



def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}

    nav = main()
    context = {nav[0]: nav[1], 'items': items, 'order': order}

    return render(request, 'store/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0}

    nav = main()
    context = {nav[0]: nav[1], 'items': items, 'order': order}


    return render(request, 'store/checkout.html', context)