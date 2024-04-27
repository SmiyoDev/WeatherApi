# weather_app/views.py
import requests
from django.shortcuts import render


def index(request):
    # Fetch other API data (outside the conditional block)
    r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    res1 = r1.json()
    fact = res1['text']

    r2 = requests.get('https://www.boredapi.com/api/activity')
    res2 = r2.json()
    activity = res2['activity']

    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']

    if request.method == 'POST':
        # Handle form submission
        city = request.POST.get('city_name')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=94145628a34c3d75af576238117c8b31'
        city_weather = requests.get(url).json()
        # Process the weather data as needed

        return render(request, 'templates/index.html', {
            'fact': fact,
            'activity': activity,
            'dog': dog,
            'city_weather': city_weather,
        })
    else:
        # Render the initial form
        return render(request, 'templates/index.html', {
            'fact': fact,
            'activity': activity,
            'dog': dog,
        })
