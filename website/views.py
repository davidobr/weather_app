from django.shortcuts import render
import requests
import api_key as key

api_key = key.API


def homepage(request):
    if request.method == "POST":
        city = request.POST.get('city')  # Replace 'city' with the name of your form input field
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        return render(request, 'website/homepage.html', {'weather_data': weather_data})
    else:
        return render(request, 'website/homepage.html')
