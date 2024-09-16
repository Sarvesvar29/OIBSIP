import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,  
        'appid': api_key,
        'units': 'metric' 
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']

            # Display weather information
            print(f"Weather in {city}, {country}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather_desc.capitalize()}")
        else:
            print(f"Error: {data['message'].capitalize()}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    api_key = "1dbc888e556e4ea11f2011b7c670f533"
    
    print("Welcome to the Weather App!")

    location = input("Enter city name or ZIP code: ")
    
    get_weather(api_key, location)
