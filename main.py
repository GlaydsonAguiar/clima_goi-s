from etl.extract import get_weather_data
from etl.transform import transform_weather_data
from etl.load import save_to_csv

API_KEY = '2979be9d3548931e38654c8b4cdc2017'

cities = [
    'Goiânia',
    'Anápolis',
    'Aparecida de Goiânia',
    'Rio Verde',
    'Luziânia',
    'Águas Lindas de Goiás',
    'Valparaíso de Goiás',
    'Trindade',
    'Formosa',
    'Catalão'
]

for city in cities:
    raw = get_weather_data(city, API_KEY)
    if raw:
        clean = transform_weather_data(raw)
        save_to_csv(clean)


        

