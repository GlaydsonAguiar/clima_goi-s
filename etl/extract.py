import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},BR&appid={api_key}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar dados de {city}: {response.status_code}")
        return None
