def transform_weather_data(raw_data):
    return {
        "cidade": raw_data["name"],
        "temperatura": raw_data["main"]["temp"],
        "umidade": raw_data["main"]["humidity"],
        "descricao": raw_data["weather"][0]["description"],
        "vento_kmh": raw_data["wind"]["speed"]
    }
